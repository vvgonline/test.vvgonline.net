using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;
using VVG.Web.Models;

namespace VVG.Web.Services
{
    public class MetadataService
    {
        private readonly HttpClient _http;
        private Metadata? _metadata;
        private TwitterCard? _twitterCard;
        private OpenGraph? _openGraph;
        private string? _jsonLd;

        public PageMetadata PageMetadata { get; private set; } = new PageMetadata();
        public event Action? OnMetadataChanged;

        public void SetPageMetadata(PageMetadata newMetadata)
        {
            PageMetadata = newMetadata;
            OnMetadataChanged?.Invoke();
        }

        public MetadataService(HttpClient http)
        {
            _http = http;
        }

        public async Task<Metadata?> GetMetadataAsync()
        {
            if (_metadata == null)
            {
                _metadata = await _http.GetFromJsonAsync<Metadata>("assets/data/metadata.json");
            }
            return _metadata;
        }

        public async Task<TwitterCard?> GetTwitterCardAsync()
        {
            if (_twitterCard == null)
            {
                _twitterCard = await _http.GetFromJsonAsync<TwitterCard>("assets/data/twitter-card.json");
            }
            return _twitterCard;
        }

        public async Task<OpenGraph?> GetOpenGraphAsync()
        {
            if (_openGraph == null)
            {
                _openGraph = await _http.GetFromJsonAsync<OpenGraph>("assets/data/open-graph.json");
            }
            return _openGraph;
        }

        public async Task<string?> GetJsonLdAsync()
        {
            if (_jsonLd == null)
            {
                _jsonLd = await _http.GetStringAsync("assets/data/json-ld.json");
            }
            return _jsonLd;
        }
    }
}
