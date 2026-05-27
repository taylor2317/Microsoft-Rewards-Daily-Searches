import time
import pyautogui

# List of words
words = [
    "apple", "mountain", "river", "lantern", "forest", "mirror", "castle",
    "whisper", "ocean", "thunder", "pencil", "galaxy", "window", "candle",
    "meadow", "planet", "bridge", "sunrise", "shadow", "blanket", "feather",
    "rocket", "diamond", "volcano", "harvest", "notebook", "island",
    "tornado", "library", "waterfall", "backpack", "horizon", "jungle",
    "compass", "firefly", "rainstorm", "pyramid", "snowflake", "treasure",
    "wildflower", "starlight", "dragon", "vineyard", "campfire", "paradise",
    "lighthouse", "canyon", "satellite", "breeze", "watermelon", "pearl",
    "avalanche", "skylight", "carousel", "pioneer", "painting", "microscope",
    "fireplace", "planetarium", "sunflower", "raindrop", "seashell",
    "marble", "festival", "journey", "telescope", "vine", "butterfly",
    "coconut", "suitcase", "orchestra", "fountain", "daydream", "blueberry",
    "keyboard", "adventure", "hammock", "penguin", "pineapple", "cinnamon",
    "moonlight", "starfish", "windmill", "desert", "jacket", "guitar",
    "parrot", "pavilion", "sandcastle", "jellyfish", "quartz", "carnation",
    "staircase", "sketchbook", "raindance", "mushroom", "cobblestone",
    "picnic", "watercolor", "hurricane", "teacup", "origami", "snowstorm",
    "wagon", "hedgehog", "balloon", "cupcake", "trumpet", "strawberry",
    "bluejay", "emerald", "waterfront", "camouflage", "iceberg", "meerkat",
    "volleyball", "raincoat", "typewriter", "scarecrow", "lullaby",
    "raccoon", "shoelace", "cactus", "moonbeam", "tangerine", "sledding",
    "koala", "driftwood", "porcelain", "airplane", "caterpillar",
    "wateringcan", "wildfire", "snowman", "harmonica", "dragonfly", "tulip",
    "cabin", "waterwheel", "fireworks", "pancake", "peppermint", "mosaic",
    "pebble", "igloo", "ladder", "beacon", "honeycomb", "violin",
    "hourglass", "rainbow", "sapphire", "seahorse", "echo", "barnacle",
    "pinecone", "maple", "anchor", "riddle", "zeppelin", "magnolia",
    "postcard", "cliffside", "tortoise", "flamingo", "campground", "copper",
    "riverside", "paperclip", "moonstone", "griffin", "seagull",
    "dreamcatcher", "toothbrush", "cereal", "starburst", "wheelbarrow",
    "beetle", "nectarine", "laneway", "frostbite", "silverware", "cavern",
    "brickwork", "musicbox", "riverbank", "measuringcup", "nightfall",
    "shoebox", "canopy", "jigsaw", "oakwood", "harbor", "wildberry",
    "sunbeam", "treetop", "dandelion", "peppercorn", "wilderness",
    "riverboat", "skateboard", "drumstick", "quicksand", "storybook",
    "crescent", "lilypad", "turbine", "cupboard", "wanderer"
]

search_interval = 5

print("Starting in 5 seconds. Switch to your browser window.")
time.sleep(5)

for word in words:
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)

    pyautogui.write(word, interval=0.05)
    pyautogui.press('enter')

    print(f"Searching Bing for: {word}")

    time.sleep(search_interval)

print("Finished running searches.")