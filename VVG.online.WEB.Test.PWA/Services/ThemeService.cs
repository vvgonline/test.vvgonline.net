public class ThemeService
{
    private string currentTheme = "light";
    public event Action? OnThemeChanged;

    public string CurrentTheme
    {
        get => currentTheme;
        set
        {
            if (currentTheme != value)
            {
                currentTheme = value;
                OnThemeChanged?.Invoke();
            }
        }
    }

    public void ToggleTheme()
    {
        CurrentTheme = CurrentTheme == "light" ? "dark" : "light";
    }
}
