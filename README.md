# Meta Tags

The meta tags for the application are handled dynamically. The `MetaTags` component, located in `src/Shared/MetaTags.razor`, is responsible for rendering the meta tags in the `<head>` of the document.

The `MetaTags` component uses the `MetadataService` to fetch the metadata from JSON files located in the `src/wwwroot/assets/data` folder. The `MetadataService` fetches the default metadata from `metadata.json`, `twitter-card.json`, and `open-graph.json`.

To modify the default meta tags, you can edit the JSON files in the `src/wwwroot/assets/data` folder.

To set page-specific meta tags, you can inject the `MetadataService` into your page component and call the `SetPageMetadata` method. For example:

```csharp
@page "/"
@inject VVG.Web.Services.MetadataService MetadataService

<PageTitle>Home</PageTitle>

@code {
    protected override void OnInitialized()
    {
        MetadataService.SetPageMetadata(new PageMetadata
        {
            Title = "VVG ONLINE — Home",
            Description = "VVG ONLINE digital business consulting",
            Keywords = "digital,consulting,ai,transformation"
        });
    }
}
```

The `PageMetadata` object has properties for the title, description, keywords, image, and Open Graph and Twitter Card data.