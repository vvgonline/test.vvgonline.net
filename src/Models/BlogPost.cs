namespace VVG.Web.Models;

public class BlogPost
{
    public string? Title { get; set; }
    public string? Slug { get; set; }
    public DateTime PublishedAt { get; set; }
    public string[]? Tags { get; set; }
    public string? Excerpt { get; set; }
    public bool Draft { get; set; }
    public string? Category { get; set; }
    public bool Featured { get; set; }
    public int TimeToRead { get; set; }
}
