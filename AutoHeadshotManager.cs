using System;

namespace GameFeatureManager
{
    public class AutoHeadshotManager
    {
        public bool AutoHeadshotEnabled { get; private set; }
        public bool SpeedIncreaserEnabled { get; private set; }
        public bool InvisibleAvatarEnabled { get; private set; }

        public void ToggleFeature(string feature, bool enabled)
        {
            switch (feature)
            {
                case "AutoHeadshot":
                    AutoHeadshotEnabled = enabled;
                    Console.WriteLine($"Auto Headshot is now {(AutoHeadshotEnabled ? "enabled" : "disabled")}");
                    break;
                case "SpeedIncreaser":
                    SpeedIncreaserEnabled = enabled;
                    Console.WriteLine($"Speed Increaser is now {(SpeedIncreaserEnabled ? "enabled" : "disabled")}");
                    break;
                case "InvisibleAvatar":
                    InvisibleAvatarEnabled = enabled;
                    Console.WriteLine($"Invisible Avatar is now {(InvisibleAvatarEnabled ? "enabled" : "disabled")}");
                    break;
                default:
                    Console.WriteLine("Unknown feature");
                    break;
            }

            // Implement logic to apply these changes in your game
            ApplyChanges();
        }

        private void ApplyChanges()
        {
            // Example implementation of how to apply changes
            if (AutoHeadshotEnabled)
            {
                // Code to enable auto-headshot in the game
            }

            if (SpeedIncreaserEnabled)
            {
                // Code to increase speed in the game
            }

            if (InvisibleAvatarEnabled)
            {
                // Code to make the avatar invisible in the game
            }
        }
    }
}
