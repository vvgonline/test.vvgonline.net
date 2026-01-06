using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using VVG.Web;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });
builder.Services.AddScoped<VVG.Web.Services.MetadataService>();
builder.Services.AddScoped<VVG.Web.Services.ThemeService>();

Console.WriteLine("Starting Blazor WebAssembly App");

await builder.Build().RunAsync();
