from typing import List
import random

chirps = [
    "Your life's so fuckin' pathetic I ran a charity 15K to raise awareness for it!",
    'Give yer balls a tug!',
    'Give yer balls a tug, titfucker!',
    'Ya titfucker!',
    'Titfucker!',
    'Fight me, see what happens!',
    'Tell your mom to top up the cell phone she bought me so I can FaceTime her late night!',
    "Fuck your whole fuckin' life!",
    "Let's get some fuckin' gyozas!",
    "Your mom loves buttplay like I like Häagen-Dazs, let's get some fuckin' ice cream!",
    'Fuck your entire fucking life ya piece of shit!',
    'Make yourselves useful, grab me a bag of dill picklers!',
    'Fuck you all, your lives are so sad, I get a charity tax break just for hanging out with ya! Nice sweep, no sweep, give yer balls a tug!',
    'The fuck you looking at, ya titfucker? Give yer balls a tug!',
    "Nice fuckin' bird cage. At the end of the day, what are you really protecting?",
    "Great day for competitive men's hockey, eh. What's women's hockey like? Same things, less competitive or what?",
    "First puck of the campaign, boys. Fuckin' get involved!",
    "You skate like a fuckin' girl, birdcage. No, you're not. Are you really? Holy fuck.",
    'Good shift, Cuteness!',
    'We should change our Facebook status to "It\'s complicated".',
    "Hey, what's your favorite kind of pizza, Cuteness? Mine's pizza ass.",
    'Short shifts!',
    "Hey, you look like that broad from The Hunger Games. I'm gonna call you Cuteness Everdeen. You like edamame?",
    'You like edamame?',
    "Fuck you, {}, go scoop my shirt off your mom's bedroom floor! She gives my nipples butterfly kisses!",
    "Fuck you, {}, your breath is an existential crisis! It made me question my whole fuckin' life!",
    'Fuck you, {}, I made your mum so wet that Trudeau deployed a 24-hour infantry unit to stack sandbags around my bed!',
    "Fuck you, {}, your mum liked one of my Instagram posts from 2 years ago in Puerto Vallarta! Tell her I'll put my swim trunks on for her any time she likes!",
    "Fuck you, {}, tell your mum I drained the bank account she set up for me. Top it up so I can get some fuckin' KFC!",
    "Fuck you, {}, your mom ugly cried because she left the lens cap on the camcorder last night! It's fuckin' amateur hour over there!",
    'Fuck you, {}, your mum shot cum straight across the room and killed my Siamese fighting fish! Threw off the pH levels in my aquarium, you piece of shit!',
    'Fuck you, {}, I made your mom cum so hard, they made a Canadian Heritage Minute out of it and Don McKellar played my dick!',
    "Fuck you, {}, you shoulda heard your mom last night, she sounded like a window closing on a Tonkinese cat's tail; she sounded like: AAAAAA^AAAAAAA^AAAAAAA!",
    'Fuck you, {}, you shoulda heard your mom last night, she sounded like my great-aunt when I pull a surprise visit; she sounded like: OOOOOO^OOOOOOO^OOOOOOH!',
    "Fuck you, {}, your mum groped me two Halloweens ago, shut the fuck up or I'll take it to Twitter!",
    'Fuck you, {}, fight me, see what happens!',
    'Fuck you, {}, tell your mom to give me a time out! Last time I tried that, she threatened to take a header on me into an empty pool at the Quality Suites!',
    "Fuck you, {}, tell your mom to leave me alone, she's been laying in my fuckin' water bed since Labour Day!",
    "Fuck you, {}! Your mom pulled the goalie on me and now she's preggo. Surprise, son, go rake the fucking yard.",
    'Fuck you, {}! I slipped one past your mom, too. Her prego farts smell like hot dog water!',
    "Fuck you, {}, I talked your mom into a three-way with our midwife and she gassed us both out of the room. I'm fuckin' humiliated!",
    "Fuck you, {}, your mom wants to name the baby after the place it was conceived. Can't wait to meet Martha's Vineyard Shore.",
    "Fuck you, {}, your mom keeps trying to slip a finger in my bum but I keep telling her I only let {}'s mom do that, ya fuckin' loser!",
    "Hey {}, I made an oopsie, can you ask your mom to pick up {}'s mom on the way over to my place? I double-booked them by mistake, you fuckin' loser!",
    "Fuck you, {}, your mom sneaky gushed so hard, she fucked me off the water bed last night! Don't tell her I was thinking about {}'s mum the entire time!",
    "Will you two just man up and make out? I started an office pool for it and the day I picked is tomorrow. Get tuggin', tit fuckers!",
    "Fuck you, {}! Your mom's in her first trimester and already bitching about baby brain. Had to tell her she's been dumber than {}'s mom since the genesis!",
    "Fuck you, {}, take a look at me! I'm not even a ref, I'm a fucking linesman, but you can refereef on my nuts any time ya piece of shit!",
]

happen_chirps = [
    'Three things: I hit you, you hit the pavement, ambulance hits sixty!',
    "Three things: I hit you, you hit the pavement, I jerk off on your driver's side door handle again!",
    'Three things: I hit you, you hit the pavement, I fuck your mom again!',
]


def get_random_chirp(user_mention: str,
                     other_mention: str = random.choice(['Reilly', 'Jonesy'])) -> str:
    """Generates a random chirp, filling in names as necessary.

    Args:
        user_mention (str): The target of the chirp, in the form of a name, or a Slack/Discord "mention" string
        other_mention (str, optional): Some chirps have two targets, so you can optionally fill this in to customize both. Otherwise, it picks either "Reilly" or "Jonesy" at random.

    Returns:
        str: the chirp
    """
    chirp_template = random.choice(chirps)
    return chirp_template.format(user_mention, other_mention)


def get_happen_chirp() -> str:
    """Simpler, more specific case of `get_random_chirp`. Generates a random response to "oh yeah, what's gonna happen?"

    Returns:
        str: the chirp
    """
    return random.choice(happen_chirps)