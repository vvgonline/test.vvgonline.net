using System.Net.Http.Json;

public class DataService
{
    private readonly HttpClient _httpClient;
    private List<Service>? _services;
    private List<BlogPost>? _blogPosts;
    private object? _statistics;

    public DataService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<List<Service>> GetServices()
    {
        if (_services == null)
        {
            var response = await _httpClient.GetAsync("data/services.json");
            var data = await response.Content.ReadFromJsonAsync<ServiceResponse>();
            _services = data?.Services ?? new List<Service>();
        }
        return _services!;
    }

    public async Task<List<BlogPost>> GetBlogPosts()
    {
        if (_blogPosts == null)
        {
            var response = await _httpClient.GetAsync("data/blog-posts.json");
            var data = await response.Content.ReadFromJsonAsync<BlogResponse>();
            _blogPosts = data?.Posts ?? new List<BlogPost>();
        }
        return _blogPosts!;
    }

    public async Task<BlogPost?> GetBlogPostBySlug(string slug)
    {
        var posts = await GetBlogPosts();
        return posts.FirstOrDefault(p => p.Slug == slug);
    }

    public async Task<object?> GetStatistics()
    {
        if (_statistics == null)
        {
            var response = await _httpClient.GetAsync("data/facts-figures.json");
            _statistics = await response.Content.ReadFromJsonAsync<object>();
        }
        return _statistics;
    }
}

// Response Models
public class ServiceResponse { public List<Service> Services { get; set; } = new(); }
public class BlogResponse { public List<BlogPost> Posts { get; set; } = new(); }
