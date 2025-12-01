using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using VVG.online.WEB.Test.PWA;
using System.Globalization;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });

// App services used by components
builder.Services.AddSingleton<ThemeService>();
builder.Services.AddSingleton<LanguageService>();
builder.Services.AddScoped<DataService>();

// Set default culture
CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("en-IN");
CultureInfo.DefaultThreadCurrentUICulture = new CultureInfo("en-IN");

await builder.Build().RunAsync();
