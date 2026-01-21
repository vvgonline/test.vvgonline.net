using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using Microsoft.JSInterop;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Linq;

namespace VVG.Web.Layout
{
    public partial class MainLayout : LayoutComponentBase, IAsyncDisposable
    {
        [Inject] private IJSRuntime JS { get; set; } = null!;
        [Inject] private Services.ThemeService ThemeService { get; set; } = null!;
        [Inject] private HttpClient Http { get; set; } = null!;

        private ElementReference mainLayoutDiv;
        private DotNetObjectReference<MainLayout>? _dotNetHelper;

        public bool isTerminalOpen = false;
        private List<ChatMessage> _chatHistory = new();
        private string _userInput = "";
        private bool _isModelLoading = true;
        private string _systemPrompt = "";
        private string _knowledgeBaseContext = "";
        private const int MaxHistory = 10; // Keep the last 10 messages

        protected override async Task OnInitializedAsync()
        {
            _dotNetHelper = DotNetObjectReference.Create(this);
            await ThemeService.InitializeThemeAsync();
            _chatHistory.Add(new ChatMessage { Role = "assistant", Content = "// Connecting to VIKAS AI Agent..." });

            // Start both tasks concurrently
            var knowledgeBaseTask = LoadKnowledgeBase();
            var initTask = InitializeChat();

            await Task.WhenAll(knowledgeBaseTask, initTask);

            // This logic will be moved to the JS callback
            _isModelLoading = false;
            _chatHistory.Add(new ChatMessage { Role = "assistant", Content = "// SECURE CONNECTION ESTABLISHED." });
            _chatHistory.Add(new ChatMessage { Role = "assistant", Content = "// AGENT READY. HOW CAN I ASSIST YOU?" });
            StateHasChanged();
        }

        private async Task InitializeChat()
        {
            try
            {
                // Pass the DotNetObjectReference to JavaScript
                await JS.InvokeVoidAsync("transformersChat.init", _dotNetHelper);
            }
            catch (Exception ex)
            {
                UpdateProgress($"// Error: {ex.Message}");
            }
        }

        private async Task LoadKnowledgeBase()
        {
            _systemPrompt = "You are Vikas, a helpful and friendly AI assistant for the VVG Online website. Your goal is to help users by answering questions based *only* on the provided context about blog posts and services. Be concise. If the answer is not in the context, say that you do not have information on that topic. Do not mention the context in your response.";

            var blogFiles = new[]
            {
                "Communication-Mastery-for-Digital-Business-Success.md", "Digital-Assets-The-Real-Estate-of-the-Virtual-World.md",
                "Don-t-Normalize-Common-Things-A-Philosophy-for-Business-Excellence.md", "GST-Rate-Deductions-for-E-commerce-A-Complete-Guide-by-VVG-ONLINE.md",
                "Key-Performance-Indicators-KPIs.md", "Operating-Model-Design.md", "The-Digital-Marketing-Investment-Imperative.md"
            };

            var sb = new StringBuilder();
            sb.AppendLine("### CONTEXT FROM WEBSITE ###");
            foreach (var file in blogFiles)
            {
                try
                {
                    var content = await Http.GetStringAsync($"assets/data/blogs/{file}");
                    sb.AppendLine($"--- Content from {file.Replace(".md", "")} ---");
                    sb.AppendLine(content);
                }
                catch (System.Exception ex)
                {
                    _chatHistory.Add(new ChatMessage { Role = "assistant", Content = $"// Error loading knowledge file: {file}" });
                }
            }
            sb.AppendLine("### END OF CONTEXT ###");
            _knowledgeBaseContext = sb.ToString();
        }

        private async Task HandleTerminalInput(KeyboardEventArgs e)
        {
            if (e.Key != "Enter" || string.IsNullOrWhiteSpace(_userInput)) return;

            var userMessageText = _userInput;
            _chatHistory.Add(new ChatMessage { Role = "user", Content = userMessageText });
            _userInput = "";
            StateHasChanged();
            await ScrollToBottom();

            // Construct the message list to send to JS
            var messagesForJs = new List<JsChatMessage>
            {
                new() { Role = "system", Content = $"{_systemPrompt}\n{_knowledgeBaseContext}" }
            };

            // Add recent history
            messagesForJs.AddRange(_chatHistory
                .Where(m => m.Role != "system") // Don't duplicate system prompt
                .TakeLast(MaxHistory)
                .Select(m => new JsChatMessage { Role = m.Role, Content = m.Content }));

            var response = await JS.InvokeAsync<string>("transformersChat.generate", messagesForJs);

            _chatHistory.Add(new ChatMessage { Role = "assistant", Content = response });
            StateHasChanged();
            await ScrollToBottom();
        }

        private async Task ScrollToBottom()
        {
            try
            {
                await JS.InvokeVoidAsync("eval", "document.getElementById('chat-output').scrollTop = document.getElementById('chat-output').scrollHeight");
            }
            catch (JSException) { /* Bury JS exceptions if element is not ready */ }
        }

        public void ToggleTerminal() => isTerminalOpen = !isTerminalOpen;
        public void HandleKeyDown(KeyboardEventArgs e)
        {
            if (e.Key == "F10") ToggleTerminal();
        }

        public async ValueTask DisposeAsync() { /* Nothing to dispose in this version */ }

        // Used for UI binding
        public class ChatMessage
        {
            public string Role { get; set; } = "";
            public string Content { get; set; } = "";
        }

        // Used for JS interop serialization
        public class JsChatMessage
        {
            public string Role { get; set; } = "";
            public string Content { get; set; } = "";
        }

        // Add these methods to MainLayout.razor.cs

        [JSInvokable]
        public void UpdateProgress(string message)
        {
            // Update the last system message or add new one
            if (_chatHistory.Count > 0 && _chatHistory.Last().Role == "assistant")
            {
                _chatHistory.Last().Content = message;
            }
            else
            {
                _chatHistory.Add(new ChatMessage { Role = "assistant", Content = message });
            }
            StateHasChanged();
        }

        [JSInvokable]
        public void OnModelReady()
        {
            _isModelLoading = false;
            _chatHistory.Add(new ChatMessage { Role = "assistant", Content = "// SECURE CONNECTION ESTABLISHED." });
            _chatHistory.Add(new ChatMessage { Role = "assistant", Content = "// AGENT READY. HOW CAN I ASSIST YOU?" });
            StateHasChanged();
        }
    }
}
