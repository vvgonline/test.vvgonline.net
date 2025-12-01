public class BlogPost
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public string Slug { get; set; } = "";
    public string Author { get; set; } = "";
    public string Date { get; set; } = "";
    public int ReadTime { get; set; }
    public List<string> Tags { get; set; } = new();
    public string Category { get; set; } = "";
    public string Excerpt { get; set; } = "";
    public string FeaturedImage { get; set; } = "";
    public string Content { get; set; } = "";
    public string Keywords { get; set; } = "";
}
