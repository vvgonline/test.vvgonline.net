public class Service
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public string ShortTitle { get; set; } = "";
    public string Description { get; set; } = "";
    public string FullDescription { get; set; } = "";
    public string Icon { get; set; } = "";
    public List<string> Benefits { get; set; } = new();
    public string Category { get; set; } = "";
}
