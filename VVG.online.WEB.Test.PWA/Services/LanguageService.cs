public class LanguageService
{
    private string currentLanguage = "en";
    public event Action? OnLanguageChanged;

    public string CurrentLanguage
    {
        get => currentLanguage;
        set
        {
            if (currentLanguage != value)
            {
                currentLanguage = value;
                OnLanguageChanged?.Invoke();
            }
        }
    }

    public void Toggle()
    {
        CurrentLanguage = CurrentLanguage.Equals("en", StringComparison.OrdinalIgnoreCase) ? "hi" : "en";
    }

    public Dictionary<string, string> Translations = new()
    {
        { "home", "Home" },
        { "services", "Services" },
        { "blog", "Blog" },
        { "presentations", "Presentations" },
        { "contact", "Contact" },
        { "search", "Search" },
        // Add more translations
    };

    public string Translate(string key)
    {
        return Translations.ContainsKey(key) ? Translations[key] : key;
    }
}
