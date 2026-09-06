"""
Comprehensive Animal Knowledge Base for the 90-Class Dataset.
Provides encyclopedic facts, scientific names, habitats, diets, conservation status,
and spoken narration scripts for Text-to-Speech.
"""

ANIMAL_INFO = {
    "antelope": {
        "scientific_name": "Alcelaphinae / Bovidae",
        "diet": "Herbivore (Grasses, shoots, leaves)",
        "habitat": "Savannahs, grasslands, and deserts of Africa and Eurasia",
        "status": "Least Concern to Critically Endangered (by species)",
        "lifespan": "10 - 20 years",
        "summary": "Antelopes are graceful, agile herbivorous mammals known for their slender legs, incredible leaping ability, and permanent unbranched horns. They can reach speeds over 80 km/h to escape predators like cheetahs and lions.",
        "fun_fact": "Antelopes have specialized hollow hairs that insulate them from extreme desert heat and cold nights.",
        "speech": "This image shows an Antelope. Antelopes are swift, graceful herbivores known for their spiraled horns and astonishing leaping ability. They inhabit grasslands and savannahs, using incredible sprinting speeds to outrun predators."
    },
    "badger": {
        "scientific_name": "Meles meles / Mustelidae",
        "diet": "Omnivore (Earthworms, insects, rodents, roots, berries)",
        "habitat": "Forests, meadows, and open countryside across Europe, Asia, and North America",
        "status": "Least Concern",
        "lifespan": "8 - 14 years",
        "summary": "Badgers are short-legged, muscular mammals with distinctive black-and-white facial stripes. They are powerful diggers that build extensive underground tunnel systems known as setts, which can be passed down for generations.",
        "fun_fact": "A single badger sett can have dozens of chambers, hundreds of meters of tunnels, and multiple family generations living together.",
        "speech": "This animal is a Badger. Badgers are sturdy, tenacious burrowers recognized by their bold black and white stripes. They use their formidable claws to dig elaborate subterranean tunnels called setts."
    },
    "bat": {
        "scientific_name": "Chiroptera",
        "diet": "Insectivore / Frugivore (Insects, fruit, nectar)",
        "habitat": "Caves, hollow trees, and buildings worldwide except polar regions",
        "status": "Varies by species",
        "lifespan": "10 - 30 years",
        "summary": "Bats are the only true flying mammals on Earth. Most species navigate and hunt in total darkness using echolocation, emitting ultrasonic pulses and listening to returning echoes to detect obstacles and prey.",
        "fun_fact": "A single brown bat can catch and eat up to 1,000 mosquito-sized insects in just one hour!",
        "speech": "This is a Bat. Bats are the only mammals capable of true sustained flight. Most bats hunt in pitch darkness using echolocation, and play a vital ecological role by pollinating plants and consuming millions of insect pests."
    },
    "bear": {
        "scientific_name": "Ursidae",
        "diet": "Omnivore (Berries, fish, small mammals, roots)",
        "habitat": "Forests, tundras, and mountains across North America, Europe, and Asia",
        "status": "Vulnerable to Least Concern",
        "lifespan": "20 - 30 years",
        "summary": "Bears are large, powerful apex mammals equipped with thick fur coats, strong claws, and an acute sense of smell that surpasses even bloodhounds. Many northern bear species undergo winter dormancy or torpor.",
        "fun_fact": "A bear's sense of smell is estimated to be 7 times stronger than a bloodhound's and 2,000 times stronger than a human's.",
        "speech": "This animal is a Bear. Bears are remarkably intelligent and powerful mammals with non-retractable claws, dense fur, and an extraordinary sense of smell that can detect food from miles away."
    },
    "bee": {
        "scientific_name": "Anthophila / Hymenoptera",
        "diet": "Herbivore (Nectar and pollen)",
        "habitat": "Meadows, orchards, gardens, and flowering habitats worldwide",
        "status": "Vulnerable to Endangered (many species)",
        "lifespan": "6 weeks (worker) to 3 years (queen)",
        "summary": "Bees are flying social insects renowned for their crucial role in pollinating flowering plants and crops. Honeybees live in complex hives governed by a queen and communicate through intricate 'waggle dances'.",
        "fun_fact": "Honeybees communicate the exact distance and direction of distant flowers using a sophisticated waggle dance relative to the sun.",
        "speech": "This insect is a Bee. Bees are essential pollinators responsible for one-third of the world's food crops. They produce golden honey, build hexagonal wax hives, and communicate using an elaborate waggle dance."
    },
    "beetle": {
        "scientific_name": "Coleoptera",
        "diet": "Herbivore / Detritivore (Plants, decaying wood, fungi)",
        "habitat": "Every terrestrial and freshwater habitat globally",
        "status": "Least Concern",
        "lifespan": "A few months to several years",
        "summary": "Beetles make up the largest order in the animal kingdom, accounting for roughly 25% of all known animal species. They possess hardened front wings called elytra that protect their delicate flight wings.",
        "fun_fact": "One in every four described animal species on Earth is a beetle!",
        "speech": "This is a Beetle. Beetles form the most diverse group of living creatures on Earth, with over 400,000 known species. They have hardened wing shields called elytra that protect them from predators."
    },
    "bison": {
        "scientific_name": "Bison bison",
        "diet": "Herbivore (Grasses, sedges, prairie plants)",
        "habitat": "Plains, grasslands, and river valleys of North America and Europe",
        "status": "Near Threatened",
        "lifespan": "15 - 20 years",
        "summary": "Bison are the largest native land mammals in North America. Weighing up to 1,000 kg, they have massive humped shoulders, heavy brown coats, and curved horns, and can run unexpectedly fast at up to 55 km/h.",
        "fun_fact": "Despite their massive bulk, bison can jump up to 6 feet vertically and sprint faster than a horse.",
        "speech": "This animal is a Bison. Bison are colossal grazers and the largest land animals in North America, sporting heavy curved horns, a woolly winter coat, and surprising sprinting agility reaching 35 miles per hour."
    },
    "boar": {
        "scientific_name": "Sus scrofa",
        "diet": "Omnivore (Roots, tubers, acorns, small reptiles, worms)",
        "habitat": "Broadleaf deciduous forests and scrublands across Europe and Asia",
        "status": "Least Concern",
        "lifespan": "10 - 14 years",
        "summary": "Wild boars are robust, bristly-coated ancestors of domestic pigs. Equipped with sharp, protruding tusks that continuously grow and sharpen against each other, they are highly adaptable, intelligent woodland foragers.",
        "fun_fact": "A wild boar's tusks can grow up to 12 centimeters long and self-sharpen every time the boar opens and closes its mouth.",
        "speech": "This is a Wild Boar. Wild boars are tough, intelligent forest mammals recognized by their thick bristly coat and razor-sharp tusks used for rooting through forest soil and defense."
    },
    "butterfly": {
        "scientific_name": "Lepidoptera",
        "diet": "Herbivore (Flower nectar, tree sap, mineral salts)",
        "habitat": "Gardens, rainforests, meadows, and grasslands across the globe",
        "status": "Varies by species",
        "lifespan": "1 week to 9 months",
        "summary": "Butterflies are delicate winged insects famous for undergoing complete metamorphosis from egg to caterpillar, chrysalis, and adult. Their vibrant wings are covered in thousands of microscopic light-reflecting scales.",
        "fun_fact": "Butterflies actually taste food with their feet, which possess chemical receptors to test leaves for edible nutrients before laying eggs.",
        "speech": "This is a Butterfly. Butterflies are celebrated for their dazzling, colorful wings and astonishing metamorphosis from creeping caterpillars into fluttering beauties. Remarkably, butterflies taste food using receptors on their feet."
    },
    "cat": {
        "scientific_name": "Felis catus",
        "diet": "Carnivore (Meat, fish, poultry)",
        "habitat": "Domestic homes, farms, and urban settings worldwide",
        "status": "Domesticated",
        "lifespan": "12 - 18 years",
        "summary": "Domestic cats are agile, carnivorous companions cherished for their sleek bodies, flexible spines, sharp retractable claws, and keen night vision. They communicate through purrs, meows, and body language.",
        "fun_fact": "Cats can rotate their ears 180 degrees independently and spend around 70 percent of their lives sleeping.",
        "speech": "This is a Cat. Domestic cats are among the world's most beloved companion animals, famous for their lightning reflexes, purring, retractable claws, and ability to see in near-total darkness."
    },
    "caterpillar": {
        "scientific_name": "Lepidoptera (larval stage)",
        "diet": "Herbivore (Foliage, leaves, flowers)",
        "habitat": "Plants, shrubs, gardens, and trees worldwide",
        "status": "Least Concern",
        "lifespan": "2 - 5 weeks (before pupation)",
        "summary": "A caterpillar is the larval stage of a butterfly or moth. Equipped with voracious appetites, caterpillars eat almost continuously, multiplying their body weight thousands of times before building a cocoon or chrysalis.",
        "fun_fact": "A caterpillar has around 4,000 muscles in its tiny body, compared to roughly 650 muscles in a human being.",
        "speech": "This is a Caterpillar. Caterpillars are the larval form of butterflies and moths. They spend their days consuming leaves at high speed to store the immense energy needed to undergo metamorphosis."
    },
    "chimpanzee": {
        "scientific_name": "Pan troglodytes",
        "diet": "Omnivore (Fruits, leaves, nuts, insects, small mammals)",
        "habitat": "Tropical rainforests and savannahs of equatorial Africa",
        "status": "Endangered",
        "lifespan": "35 - 50 years",
        "summary": "Chimpanzees are humanity's closest living evolutionary relatives, sharing nearly 99% of our DNA. They exhibit sophisticated social hierarchies, emotional depth, communication gestures, and complex tool usage.",
        "fun_fact": "Chimpanzees regularly craft and use tools, such as stripping twigs to 'fish' for termites or using heavy stones to crack open hard nuts.",
        "speech": "This is a Chimpanzee. Chimpanzees are intelligent great apes that share roughly 99 percent of our DNA. They form complex communities, use tools, and express deep emotional bonds."
    },
    "cockroach": {
        "scientific_name": "Blattodea",
        "diet": "Omnivore / Detritivore (Decaying matter, starch, organic debris)",
        "habitat": "Warm, humid environments and urban buildings worldwide",
        "status": "Least Concern",
        "lifespan": "1 - 2 years",
        "summary": "Cockroaches are ancient, extraordinarily hardy insects that have survived for over 300 million years. They can withstand high radiation, squeeze through microscopic cracks, and survive without food for a month.",
        "fun_fact": "A cockroach can survive for over a week without its head because its circulatory system is open and it breathes through spiracles along its body.",
        "speech": "This is a Cockroach. Cockroaches are among the most resilient organisms on the planet, having survived for over 300 million years. They can squeeze through tiny crevices and survive weeks without food."
    },
    "cow": {
        "scientific_name": "Bos taurus",
        "diet": "Herbivore (Grasses, hay, grains)",
        "habitat": "Pastures, grasslands, and agricultural farms globally",
        "status": "Domesticated",
        "lifespan": "15 - 20 years",
        "summary": "Cows are gentle ruminant livestock that play a central role in agriculture worldwide. They have a four-chambered stomach (including the rumen) designed to ferment and digest tough plant cellulose.",
        "fun_fact": "Cows have best friends among their herd and become visibly stressed when separated from them.",
        "speech": "This is a Cow. Domestic cattle are gentle ruminant grazers with four-chambered stomachs designed to digest grasses. Cows are highly social herd animals that form lasting friendships with other herd members."
    },
    "coyote": {
        "scientific_name": "Canis latrans",
        "diet": "Carnivore / Omnivore (Rodents, rabbits, fruit, carrion)",
        "habitat": "Plains, forests, deserts, and suburban neighborhoods of North America",
        "status": "Least Concern",
        "lifespan": "10 - 14 years",
        "summary": "Coyotes are remarkably versatile wild canines native to North America. Known as the 'trickster' in folklore, their eerie, high-pitched howls and yips resonate across prairies and deserts at dusk.",
        "fun_fact": "Coyotes can run at speeds up to 69 km/h and can jump over an 8-foot fence from a standing start.",
        "speech": "This is a Coyote. Coyotes are cunning, highly adaptable canines found across North America. Known for their twilight howling choruses, they can flourish in habitats ranging from harsh deserts to urban parks."
    },
    "crab": {
        "scientific_name": "Brachyura",
        "diet": "Omnivore (Algae, mollusks, worms, crustaceans, detritus)",
        "habitat": "Oceans, freshwater rivers, and coastal shores worldwide",
        "status": "Least Concern",
        "lifespan": "3 - 30 years (by species)",
        "summary": "Crabs are decapod crustaceans protected by a thick, calcified exoskeleton. They possess five pairs of legs, with the front pair modified into strong pincers (chelae) used for feeding and defense.",
        "fun_fact": "Most crabs walk sideways because their leg joints bend outward, allowing them to scuttle rapidly over rocky terrain and into crevices.",
        "speech": "This is a Crab. Crabs are ten-legged crustaceans equipped with a sturdy shell and powerful pincers. Most crab species scuttle sideways because of the way their leg joints are structured."
    },
    "crow": {
        "scientific_name": "Corvus",
        "diet": "Omnivore (Seeds, berries, insects, carrion, human food)",
        "habitat": "Farmlands, open woodlands, and urban cities worldwide",
        "status": "Least Concern",
        "lifespan": "7 - 15 years",
        "summary": "Crows are all-black birds famous for their extraordinary intelligence, problem-solving skills, and complex social networks. They can recognize human faces, remember grievances, and use tools to extract food.",
        "fun_fact": "Crows recognize individual human faces and can hold a grudge for years, warning other crows in the flock about dangerous people.",
        "speech": "This bird is a Crow. Crows are among the most intelligent creatures on the planet, possessing reasoning abilities on par with a seven-year-old child. They can solve multi-step puzzles and recognize human faces."
    },
    "deer": {
        "scientific_name": "Cervidae",
        "diet": "Herbivore (Leaves, twigs, bark, fruits, mushrooms)",
        "habitat": "Forests, meadows, wetlands, and grasslands worldwide",
        "status": "Varies by species",
        "lifespan": "10 - 15 years",
        "summary": "Deer are graceful, alert hoofed ruminants. In most species, males grow impressive bone antlers that are shed and regrown annually at astonishing speeds—making antlers the fastest-growing bone tissue in the animal kingdom.",
        "fun_fact": "Deer antlers can grow up to an inch a day during spring, covered in a soft, blood-rich velvet layer.",
        "speech": "This is a Deer. Deer are graceful woodland herbivores with keen senses of hearing and smell. Male deer grow magnificent antlers each year, which represent the fastest growing bone tissue known in nature."
    },
    "dog": {
        "scientific_name": "Canis familiaris",
        "diet": "Omnivore (Meat, vegetables, grains)",
        "habitat": "Homes, working farms, and cities worldwide",
        "status": "Domesticated",
        "lifespan": "10 - 16 years",
        "summary": "Known as 'man's best friend', dogs were the first animal species domesticated by humans over 15,000 years ago. Their unparalleled loyalty, emotional intelligence, and acute senses make them cherished companions and workers.",
        "fun_fact": "A dog's nose print is as unique as a human fingerprint and can be used to identify them with complete accuracy.",
        "speech": "This is a Dog. Man's best friend and humanity's oldest companion, dogs possess a sense of smell up to 100,000 times more sensitive than ours, alongside deep emotional loyalty."
    },
    "dolphin": {
        "scientific_name": "Delphinidae",
        "diet": "Carnivore (Fish, squid, crustaceans)",
        "habitat": "Warm and temperate oceans and select river basins worldwide",
        "status": "Least Concern to Endangered (by species)",
        "lifespan": "20 - 45 years",
        "summary": "Dolphins are highly intelligent aquatic mammals known for their playful behavior, curved mouths resembling permanent smiles, and sophisticated echolocation clicks and whistles used to communicate in ocean pods.",
        "fun_fact": "Dolphins sleep with one eye open and only half their brain at a time, allowing them to surface for air while resting.",
        "speech": "This is a Dolphin. Dolphins are playful marine mammals famous for their leaping acrobatics, deep social pods, and signature echolocation clicks. Remarkably, dolphins keep one brain hemisphere awake even while asleep to breathe."
    },
    "donkey": {
        "scientific_name": "Equus africanus asinus",
        "diet": "Herbivore (Grasses, shrubs, desert scrub)",
        "habitat": "Deserts, dry grasslands, and farmlands globally",
        "status": "Domesticated",
        "lifespan": "25 - 40 years",
        "summary": "Donkeys are sturdy, sure-footed members of the horse family renowned for their stamina, patience, and intelligence. Their oversized ears help disperse desert heat and catch acoustic calls across miles of dry landscape.",
        "fun_fact": "Donkeys have an incredible memory; they can recognize areas and other donkeys they haven't seen in 25 years.",
        "speech": "This is a Donkey. Donkeys are hardy, resilient animals known for their large ears that dissipate heat, sure-footed walking on mountain trails, and a memory that can recall friends decades later."
    },
    "dragonfly": {
        "scientific_name": "Anisoptera",
        "diet": "Carnivore (Mosquitoes, flies, gnats, moths)",
        "habitat": "Lakes, ponds, rivers, and marshes worldwide",
        "status": "Least Concern",
        "lifespan": "Several months (adult)",
        "summary": "Dragonflies are ancient aerial hunters that evolved over 300 million years ago. Their four wings can move independently, allowing them to hover, fly backwards, upside down, and accelerate to 50 km/h.",
        "fun_fact": "Dragonflies are the most successful predators on Earth, with an astonishing 95% hunting kill rate.",
        "speech": "This is a Dragonfly. Dragonflies are ancient aerial master acrobats. With four independently moving wings and 360-degree compound eyes, they boast a 95% hunting success rate, surpassing lions and hawks."
    },
    "duck": {
        "scientific_name": "Anatidae",
        "diet": "Omnivore (Aquatic plants, insects, small fish, seeds)",
        "habitat": "Lakes, ponds, rivers, and coastal wetlands worldwide",
        "status": "Least Concern",
        "lifespan": "5 - 10 years",
        "summary": "Ducks are web-footed waterfowl equipped with waterproof plumage coated in protective oils. Their broad, flattened bills contain miniature strainers (pecten) that filter food particles from murky water.",
        "fun_fact": "Duck feathers are so waterproof that even when a duck dives completely underwater, its insulating down feathers stay completely dry.",
        "speech": "This bird is a Duck. Ducks are adaptable waterfowl with waterproof feathers lubricated by special preen gland oils. Their webbed feet act like paddles, allowing them to swim gracefully across lakes and rivers."
    },
    "eagle": {
        "scientific_name": "Accipitridae",
        "diet": "Carnivore (Fish, rabbits, small mammals, reptiles)",
        "habitat": "Cliffs, mountains, lakesides, and open forests worldwide",
        "status": "Least Concern to Endangered",
        "lifespan": "20 - 30 years",
        "summary": "Eagles are formidable apex raptors celebrated as symbols of majesty, strength, and freedom. They possess hooked beaks, razor-sharp talons, and vision up to 8 times sharper than human eyesight.",
        "fun_fact": "An eagle can spot a rabbit from over 3 kilometers away while soaring high in the sky.",
        "speech": "This is an Eagle. Eagles are apex birds of prey revered worldwide as symbols of courage and power. Their extraordinary eyesight is up to eight times sharper than human vision, allowing them to pinpoint prey miles away."
    },
    "elephant": {
        "scientific_name": "Elephantidae (Loxodonta / Elephas)",
        "diet": "Herbivore (Grasses, foliage, bark, fruit)",
        "habitat": "Savannahs, tropical rainforests, and scrublands of Africa and Asia",
        "status": "Endangered to Critically Endangered",
        "lifespan": "60 - 70 years",
        "summary": "Elephants are the largest living land animals on Earth. Renowned for their majestic ivory tusks, sweeping ears, and versatile prehensile trunks containing over 40,000 muscles, they display profound empathy and memory.",
        "fun_fact": "Elephants can communicate across dozens of kilometers using deep infrasonic rumbles below the limit of human hearing.",
        "speech": "This is an Elephant. Elephants are the largest terrestrial animals on Earth, celebrated for their immense intelligence, deep family bonds, and a trunk containing over 40,000 muscles capable of picking up a single blade of grass."
    },
    "flamingo": {
        "scientific_name": "Phoenicopteridae",
        "diet": "Omnivore (Algae, brine shrimp, aquatic crustaceans)",
        "habitat": "Shallow alkaline or saline lagoons, lakes, and estuaries worldwide",
        "status": "Least Concern",
        "lifespan": "20 - 30 years",
        "summary": "Flamingos are famous for their vibrant pink and crimson plumage, stilt-like legs, and S-curved necks. They feed with their heads held upside down, filtering tiny shrimp and algae rich in carotenoid pigments.",
        "fun_fact": "Flamingos are born gray or white; their feathers only turn vibrant pink due to carotenoid pigments in the shrimp and algae they consume.",
        "speech": "This bird is a Flamingo. Flamingos are iconic for their striking pink plumage and habit of resting effortlessly on one leg. Their vibrant rosy color comes entirely from carotenoid pigments found in the algae and brine shrimp they eat."
    },
    "fly": {
        "scientific_name": "Diptera",
        "diet": "Omnivore / Detritivore (Liquified organic matter, sugars)",
        "habitat": "Nearly all terrestrial habitats worldwide",
        "status": "Least Concern",
        "lifespan": "15 - 30 days",
        "summary": "True flies possess only a single pair of flight wings, with the rear wings reduced into balancing gyroscopes called halteres. Their compound eyes contain thousands of lenses that process motion at blinding speeds.",
        "fun_fact": "A housefly processes visual information roughly four times faster than humans, making it perceive our swats in slow motion.",
        "speech": "This insect is a Fly. True flies navigate aerial currents using specialized balancing organs called halteres. Their compound eyes see the world in slow motion compared to human vision, explaining their quick evasive maneuvers."
    },
    "fox": {
        "scientific_name": "Vulpes vulpes / Canidae",
        "diet": "Omnivore (Rodents, berries, insects, bird eggs)",
        "habitat": "Forests, grasslands, tundras, and urban landscapes globally",
        "status": "Least Concern",
        "lifespan": "3 - 6 years in wild",
        "summary": "Foxes are small, clever wild canines recognized by their triangular faces, pointed upright ears, and luxurious bushy tails (brushes). They are solitary hunters who can hear small rodents burrowing under deep snow.",
        "fun_fact": "Foxes use Earth's magnetic field to judge distances when diving through deep snow to catch burrowing rodents.",
        "speech": "This is a Fox. Foxes are cunning and adaptable canines recognizable by their bushy brush tails and keen hunting senses. They can detect the rustle of a mouse under heavy snow and leap gracefully to catch it."
    },
    "goat": {
        "scientific_name": "Capra hircus",
        "diet": "Herbivore (Shrubs, grasses, leaves, weeds)",
        "habitat": "Mountains, pastures, and rocky hillsides worldwide",
        "status": "Domesticated",
        "lifespan": "15 - 18 years",
        "summary": "Goats are remarkably sure-footed herbivores renowned for their climbing prowess and curious dispositions. Their rectangular horizontal pupils give them an expansive 320-degree field of peripheral vision.",
        "fun_fact": "Mountain goats have flexible, rubbery footpads with hard outer hooves that act like rock-climbing shoes, allowing them to scale near-vertical cliffs.",
        "speech": "This is a Goat. Goats are agile, inquisitive climbers equipped with rectangular pupils that grant them wide panoramic vision to spot approaching predators across mountainous rocky terrain."
    },
    "goldfish": {
        "scientific_name": "Carassius auratus",
        "diet": "Omnivore (Flakes, algae, small crustaceans, plants)",
        "habitat": "Aquariums, garden ponds, and slow-moving freshwaters",
        "status": "Domesticated",
        "lifespan": "10 - 30 years",
        "summary": "Goldfish are small freshwater members of the carp family domesticated in ancient China over a thousand years ago. In optimal spacious ponds, they can live for several decades and grow up to 40 cm long.",
        "fun_fact": "Contrary to the myth of a three-second memory, goldfish actually have a memory span of at least five months and can be trained to recognize colors and sounds.",
        "speech": "This is a Goldfish. First domesticated over a thousand years ago, goldfish are bright freshwater fish that debunk the popular myth of poor memory—they can remember information for months and recognize their owners."
    },
    "goose": {
        "scientific_name": "Anser / Branta",
        "diet": "Herbivore (Grasses, aquatic plants, grains, seeds)",
        "habitat": "Lakes, rivers, marshes, and agricultural fields worldwide",
        "status": "Least Concern",
        "lifespan": "15 - 25 years",
        "summary": "Geese are robust, vocal waterfowl celebrated for their long necks, protective nature, and iconic V-formation migrations across continents. They mate for life and fiercely defend their goslings and territory.",
        "fun_fact": "Flying in a V-formation saves migrating geese up to 70% of energy by utilizing the aerodynamic vortex created by the bird in front.",
        "speech": "This is a Goose. Geese are strong-willed, loyal waterfowl that mate for life and migrate across continents in aerodynamic V-formations to conserve flight energy over thousands of miles."
    },
    "gorilla": {
        "scientific_name": "Gorilla gorilla / Gorilla beringei",
        "diet": "Herbivore (Leaves, stems, bamboo shoots, wild celery, fruit)",
        "habitat": "Tropical rainforests and volcanic mountain slopes of central Africa",
        "status": "Critically Endangered",
        "lifespan": "35 - 40 years",
        "summary": "Gorillas are the largest living primates on Earth. Led by a dominant mature male known as a silverback, these gentle giants possess immense physical strength, rich emotional intelligence, and peaceful family groups.",
        "fun_fact": "Every gorilla has a completely unique nose print that conservationists use to identify individual apes in the wild.",
        "speech": "This is a Gorilla. Gorillas are the world's largest primates, residing in close-knit family troops led by a protective silverback. Despite their formidable power, they are peaceful and thoughtful herbivores."
    },
    "grasshopper": {
        "scientific_name": "Caelifera",
        "diet": "Herbivore (Grasses, leaves, cereal crops)",
        "habitat": "Grasslands, pastures, meadows, and agricultural fields globally",
        "status": "Least Concern",
        "lifespan": "Up to 1 year",
        "summary": "Grasshoppers are jumping insects famous for their long, muscular hind legs and acoustic songs called stridulation, produced by rubbing pegs on their hind legs against their hardened forewings.",
        "fun_fact": "A grasshopper can catapult itself forward up to 20 times its own body length without wings, equivalent to a human jumping the length of a football field.",
        "speech": "This insect is a Grasshopper. Grasshoppers are renowned for their spring-loaded hind legs capable of launching them 20 times their body length. They create their familiar summer buzzing songs by rubbing their legs against their wings."
    },
    "hamster": {
        "scientific_name": "Cricetinae",
        "diet": "Omnivore (Seeds, nuts, grains, vegetation, insects)",
        "habitat": "Semi-arid grasslands and burrows; popular pet worldwide",
        "status": "Varies by species",
        "lifespan": "2 - 3 years",
        "summary": "Hamsters are small, rotund rodents popular as companion pets. They possess expandable cheek pouches extending along their shoulders, allowing them to hoard and carry food back to underground tunnels.",
        "fun_fact": "A hamster's cheek pouches can expand to double the width of its head and carry food equivalent to 20% of its body weight.",
        "speech": "This is a Hamster. Hamsters are charming, nocturnal rodents famous for expandable cheek pouches that can stretch along their bodies to pack away and hoard seeds back to their underground nests."
    },
    "hare": {
        "scientific_name": "Lepus",
        "diet": "Herbivore (Grasses, herbs, twigs, tree bark)",
        "habitat": "Open fields, savannahs, and arctic tundras across the northern hemisphere",
        "status": "Least Concern",
        "lifespan": "4 - 8 years",
        "summary": "Hares differ from rabbits by having longer ears, larger black-tipped hind feet, and an ability to run at breathtaking speeds up to 72 km/h. They live above ground in shallow depressions called forms.",
        "fun_fact": "Unlike baby rabbits born blind and hairless in burrows, baby hares (leverets) are born fully furred with open eyes and can hop within hours.",
        "speech": "This is a Hare. Hares are lightning-fast runners capable of hitting speeds over 45 miles per hour with zig-zagging bounds. They differ from rabbits by living above ground and having longer, black-tipped ears."
    },
    "hedgehog": {
        "scientific_name": "Erinaceinae",
        "diet": "Insectivore / Omnivore (Beetles, worms, slugs, berries, frogs)",
        "habitat": "Hedgerows, woodlands, and gardens across Europe, Asia, and Africa",
        "status": "Least Concern to Vulnerable",
        "lifespan": "4 - 7 years",
        "summary": "Hedgehogs are small nocturnal mammals covered in thousands of hollow keratin quills. When threatened, a powerful circular muscle rolls their body into an impenetrable spiny defensive ball.",
        "fun_fact": "An average adult hedgehog carries between 5,000 and 7,000 protective quills that are completely painless to the hedgehog.",
        "speech": "This is a Hedgehog. Hedgehogs are spiny nocturnal insectivores beloved for their defensive habit of curling into an unassailable prickly ball when alarmed, protected by over 5,000 sharp keratin spines."
    },
    "hippopotamus": {
        "scientific_name": "Hippopotamus amphibius",
        "diet": "Herbivore (Grasses and water vegetation)",
        "habitat": "Rivers, swamps, and lakes of sub-Saharan Africa",
        "status": "Vulnerable",
        "lifespan": "40 - 50 years",
        "summary": "Hippos are colossal semi-aquatic African mammals weighing up to 1,800 kg. Despite their bulky appearance, they can outrun humans on land, and spend their days submerged to keep their sensitive skin cool and hydrated.",
        "fun_fact": "Hippos secrete a natural red-tinted fluid called 'blood sweat' that acts as an antibacterial sunscreen and moisturizer.",
        "speech": "This is a Hippopotamus. Hippos are massive semi-aquatic giants that spend their days submerged in African rivers. Despite their peaceful grazing diet, they possess terrifying canine tusks and surprising land speed."
    },
    "hornbill": {
        "scientific_name": "Bucerotidae",
        "diet": "Omnivore (Fruits, figs, insects, small reptiles)",
        "habitat": "Tropical rainforests of sub-Saharan Africa, Asia, and Melanesia",
        "status": "Vulnerable to Critically Endangered",
        "lifespan": "30 - 40 years",
        "summary": "Hornbills are tropical forest birds characterized by long, downward-curving bills often topped with an extravagant, hollow ridge called a casque, which amplifies their booming territorial calls.",
        "fun_fact": "During nesting, the female hornbill seals herself inside a hollow tree trunk with mud, leaving only a tiny slit through which the male feeds her for months.",
        "speech": "This bird is a Hornbill. Hornbills are tropical forest birds known for their oversized downcurved beaks crowned by a hollow casque that acts like a trumpet chamber to project loud jungle calls."
    },
    "horse": {
        "scientific_name": "Equus caballus",
        "diet": "Herbivore (Hay, grass, grains)",
        "habitat": "Pastures, grasslands, and farms across the globe",
        "status": "Domesticated",
        "lifespan": "25 - 30 years",
        "summary": "Horses are majestic single-toed ungulates that have shaped human history, agriculture, and transportation for millennia. Known for their speed, endurance, and deep companionship, they possess remarkable balance.",
        "fun_fact": "Horses have a 'stay apparatus' in their leg tendons that locks their joints, allowing them to sleep standing up without falling over.",
        "speech": "This is a Horse. Celebrated for their nobility, speed, and deep companionship throughout human history, horses possess exceptional balance and can even sleep peacefully while standing upright."
    },
    "hummingbird": {
        "scientific_name": "Trochilidae",
        "diet": "Nectarivore (Floral nectar and tiny gnats)",
        "habitat": "Tropical and temperate forests, meadows, and gardens of the Americas",
        "status": "Least Concern to Endangered",
        "lifespan": "3 - 5 years",
        "summary": "Hummingbirds are nature's tiniest avian wonders. Their rapid wing beats (up to 80 flaps per second) create an audible humming sound and allow them to fly backwards, upside down, and hover motionless.",
        "fun_fact": "Hummingbirds are the only birds that can fly backwards and completely upside down.",
        "speech": "This bird is a Hummingbird. Hummingbirds are iridescent marvels of flight engineering. With hearts beating over 1,200 times a minute, they can hover stationary and fly backwards to sip nectar from flowers."
    },
    "hyena": {
        "scientific_name": "Hyaenidae",
        "diet": "Carnivore (Scavenged bones, antelopes, zebras, wildebeests)",
        "habitat": "Savannahs, grasslands, and semi-deserts of Africa and Asia",
        "status": "Least Concern",
        "lifespan": "12 - 20 years",
        "summary": "Spotted hyenas are formidable, highly social predators that live in matriarchal clans of up to 80 individuals. Their bone-crushing jaws possess one of the strongest bite forces in the animal kingdom.",
        "fun_fact": "Hyena digestive acid is so strong that it can dissolve bone, teeth, and horns completely within hours.",
        "speech": "This is a Hyena. Highly intelligent and coordinated pack hunters, hyenas live in clan societies led by dominant females. Their fearsome jaws generate enough bite force to splinter and digest solid bone."
    },
    "jellyfish": {
        "scientific_name": "Medusozoa",
        "diet": "Carnivore (Fish larvae, plankton, crustaceans)",
        "habitat": "Surface waters to the deepest ocean trenches worldwide",
        "status": "Least Concern",
        "lifespan": "A few hours to several months (some immortal)",
        "summary": "Jellyfish are mesmerizing, bell-shaped gelatinous sea creatures that have drifted in Earth's oceans for over 500 million years. They have no heart, brain, or blood, relying on nerve nets to sense their environment.",
        "fun_fact": "One species of jellyfish (Turritopsis dohrnii) is biologically immortal; when stressed, it can revert back into a juvenile polyp and start its life cycle anew.",
        "speech": "This is a Jellyfish. Having drifted in oceans long before dinosaurs existed, jellyfish have no brain or blood, yet catch prey with venomous microscopic harpoons on their tentacles."
    },
    "kangaroo": {
        "scientific_name": "Macropodidae",
        "diet": "Herbivore (Grasses, herbs, shrubs)",
        "habitat": "Arid plains, scrublands, and open woodlands of Australia",
        "status": "Least Concern",
        "lifespan": "12 - 20 years",
        "summary": "Kangaroos are iconic Australian marsupials famous for their powerful hind legs, muscular balancing tails, and forward pouches where mothers carry their developing joeys for months.",
        "fun_fact": "A red kangaroo can clear over 8 meters in a single leap and reach speeds of 60 km/h, using its tail as a third leg when balancing.",
        "speech": "This is a Kangaroo. Kangaroos are the world's largest marsupials, famed for bounding across the Australian outback on spring-like hind legs while carrying tiny joeys safe inside their pouches."
    },
    "koala": {
        "scientific_name": "Phascolarctos cinereus",
        "diet": "Herbivore (Eucalyptus leaves exclusively)",
        "habitat": "Eucalyptus forests of eastern and south-eastern Australia",
        "status": "Endangered",
        "lifespan": "13 - 18 years",
        "summary": "Koalas are tree-dwelling marsupials renowned for their fluffy round ears, button noses, and relaxed lifestyle. They feed almost exclusively on fibrous eucalyptus leaves, sleeping up to 20 hours a day.",
        "fun_fact": "Koalas have unique fingerprints that are almost indistinguishable from human fingerprints, even under electron microscopes.",
        "speech": "This is a Koala. Koalas are gentle, tree-dwelling Australian marsupials that subsist almost entirely on toxic eucalyptus leaves, which provide so little caloric energy that they sleep up to 20 hours daily."
    },
    "ladybugs": {
        "scientific_name": "Coccinellidae",
        "diet": "Carnivore (Aphids, scale insects, plant mites)",
        "habitat": "Gardens, forests, meadows, and crop fields worldwide",
        "status": "Least Concern",
        "lifespan": "1 - 2 years",
        "summary": "Ladybugs (or ladybird beetles) are beloved for their glossy domed wing covers, bright red and yellow colors, and dark polka dots. They are celebrated by farmers as natural protectors that devour pest aphids.",
        "fun_fact": "A single ladybug can devour more than 5,000 crop-destroying aphids over the course of its lifetime.",
        "speech": "This insect is a Ladybug. Adored by gardeners and farmers worldwide, ladybugs sport bright polka-dotted wing shields that warn birds of their foul taste, while devouring thousands of garden pests."
    },
    "leopard": {
        "scientific_name": "Panthera pardus",
        "diet": "Carnivore (Antelopes, monkeys, deer, wild pigs)",
        "habitat": "Rainforests, savannahs, and rocky mountains across Africa and Asia",
        "status": "Vulnerable",
        "lifespan": "12 - 17 years",
        "summary": "Leopards are solitary, stealthy big cats recognized by their rosetted coats, supreme stealth, and muscular strength. They are legendary for hauling heavy prey into high tree branches away from hyenas and lions.",
        "fun_fact": "A leopard can carry a dead antelope weighing twice its own body weight straight up the trunk of a vertical tree.",
        "speech": "This is a Leopard. Renowned as the most adaptable of all big cats, leopards are agile tree climbers whose rosetted coats provide camouflage while dragging heavy prey into treetops."
    },
    "lion": {
        "scientific_name": "Panthera leo",
        "diet": "Carnivore (Zebras, wildebeest, buffaloes, warthogs)",
        "habitat": "Grasslands, scrublands, and savannahs of sub-Saharan Africa and Gir Forest, India",
        "status": "Vulnerable",
        "lifespan": "10 - 15 years",
        "summary": "Known as the 'King of the Jungle', lions are the only truly social big cats, living in cooperative prides led by related females and protected by majestic, maned males whose roars carry up to 8 km.",
        "fun_fact": "A lion's thunderous roar can be heard across open savannah from up to 8 kilometers (5 miles) away.",
        "speech": "This is a Lion. The King of Beasts and the only social feline, lions live in cooperative prides across the African savannah, announcing their territory with roars heard five miles away."
    },
    "lizard": {
        "scientific_name": "Lacertilia",
        "diet": "Insectivore / Carnivore (Insects, small reptiles, fruit)",
        "habitat": "Deserts, forests, rocky scrub, and gardens worldwide",
        "status": "Varies by species",
        "lifespan": "5 - 20 years",
        "summary": "Lizards are widespread scaly reptiles featuring dry skin, movable eyelids, and external ear openings. Many can drop their tails to escape predators and regenerate new cartilaginous appendages.",
        "fun_fact": "Geckos have millions of microscopic hairs on their toe pads that allow them to sprint upside down across glass ceilings.",
        "speech": "This is a Lizard. Lizards are cold-blooded reptiles that thrive across deserts, rocky outcrops, and tropical rainforests, possessing keen survival adaptations like color change and tail shedding."
    },
    "lobster": {
        "scientific_name": "Nephropidae",
        "diet": "Omnivore (Mollusks, worms, small fish, sea plants)",
        "habitat": "Cold ocean floors, rocky reefs, and coastal crevices",
        "status": "Least Concern",
        "lifespan": "Up to 50 - 100 years",
        "summary": "Lobsters are long-bodied marine crustaceans possessing five pairs of walking legs, with the front claws divided into a heavy crushing claw and a razor-sharp cutting pincer.",
        "fun_fact": "Lobsters can live for over a century because their cells continuously regenerate through high telomerase enzyme production.",
        "speech": "This is a Lobster. Lobsters are bottom-dwelling marine crustaceans equipped with powerful crushing claws, blue blood, and remarkable longevity that can surpass one hundred years."
    },
    "mosquito": {
        "scientific_name": "Culicidae",
        "diet": "Nectar (males/females); blood (egg-laying females)",
        "habitat": "Wetlands, stagnant waters, and humid tropical and temperate zones",
        "status": "Least Concern",
        "lifespan": "2 - 4 weeks",
        "summary": "Mosquitoes are slender flying insects with segmented bodies and needle-like proboscises. While both sexes feed on plant nectar, females require blood protein to produce their eggs.",
        "fun_fact": "Mosquitoes are attracted to people by detecting the carbon dioxide in our breath from over 50 meters away.",
        "speech": "This insect is a Mosquito. Mosquitoes are delicate yet formidable insects. While males feed strictly on flower nectar, females seek blood meals rich in protein to develop their eggs."
    },
    "moth": {
        "scientific_name": "Lepidoptera (heterocera)",
        "diet": "Herbivore (Floral nectar, fruit juice, tree sap)",
        "habitat": "Forests, meadows, and gardens worldwide",
        "status": "Least Concern",
        "lifespan": "1 - 6 months",
        "summary": "Moths are primarily nocturnal winged insects closely related to butterflies. They typically possess feathery antennae and fold their wings flat over their bodies when resting.",
        "fun_fact": "Some male silk moths can detect the pheromones of a female from more than 10 kilometers away using their feathery antennae.",
        "speech": "This is a Moth. Moths are predominantly nocturnal winged insects with feathery antennae sensitive enough to detect scent molecules drifting miles through the night air."
    },
    "mouse": {
        "scientific_name": "Mus musculus",
        "diet": "Omnivore (Grains, seeds, berries, scraps)",
        "habitat": "Grasslands, farmlands, and urban structures globally",
        "status": "Least Concern",
        "lifespan": "1 - 3 years",
        "summary": "Mice are small, agile rodents characterized by pointed snouts, round ears, and hairless tails. Their rapid breeding cycle and inquisitive nature have made them ubiquitous across the globe.",
        "fun_fact": "A mouse can squeeze its entire body through an opening as narrow as a common pencil due to its flexible ribcage and collarbone.",
        "speech": "This is a Mouse. Mice are clever, nimble rodents with extraordinary flexibility, capable of slipping through gaps no wider than a pencil to forage for seeds and grains."
    },
    "octopus": {
        "scientific_name": "Octopoda",
        "diet": "Carnivore (Crabs, clams, shrimp, small fish)",
        "habitat": "Coral reefs, pelagic waters, and deep seabed trenches worldwide",
        "status": "Least Concern",
        "lifespan": "1 - 5 years",
        "summary": "Octopuses are eight-armed cephalopods widely regarded as the most intelligent invertebrates on Earth. With three hearts, blue blood, and brain cells distributed throughout their arms, they can change color and texture in milliseconds.",
        "fun_fact": "Two-thirds of an octopus's neurons reside in its flexible arms, meaning each tentacle can taste, touch, and think semi-independently.",
        "speech": "This is an Octopus. The genius of the sea, octopuses possess three hearts, blue blood, and skin that transforms color and texture in a fraction of a second to mimic coral and rock."
    },
    "okapi": {
        "scientific_name": "Okapia johnstoni",
        "diet": "Herbivore (Tree leaves, buds, wild fungi, fruits)",
        "habitat": "Dense canopy rainforests of the Democratic Republic of Congo",
        "status": "Endangered",
        "lifespan": "20 - 30 years",
        "summary": "The okapi, often dubbed the 'forest giraffe', is the only living relative of the giraffe. It has velvety chocolate-brown fur, horizontal zebra-like leg stripes for camouflage, and a 40-cm prehensile tongue.",
        "fun_fact": "An okapi's dark bluish-black tongue is so long (over 14 inches) that it can comfortably lick its own eyelids and clean its ears.",
        "speech": "This rare animal is an Okapi. Living deep within Congolese rainforests, the okapi is the only living cousin of the giraffe, sporting zebra-like leg stripes and a tongue long enough to clean its own eyelids."
    },
    "orangutan": {
        "scientific_name": "Pongo pygmaeus / Pongo abelii",
        "diet": "Frugivore / Omnivore (Wild figs, fruit, leaves, bark, honey)",
        "habitat": "Tropical peat swamp forests of Borneo and Sumatra",
        "status": "Critically Endangered",
        "lifespan": "35 - 45 years",
        "summary": "Orangutans are peaceful, auburn-haired great apes and the largest tree-dwelling animals on Earth. Their arm span can exceed two meters, allowing them to swing gracefully through towering rainforest canopies.",
        "fun_fact": "Orangutans build an intricate, fresh sleeping nest woven from tree branches and leaves every single evening.",
        "speech": "This is an Orangutan. The 'Person of the Forest', orangutans are gentle great apes native to Borneo and Sumatra, boasting an arm span exceeding seven feet as they swing high among forest canopies."
    },
    "otter": {
        "scientific_name": "Lutrinae",
        "diet": "Carnivore (Fish, frogs, crustaceans, sea urchins)",
        "habitat": "Rivers, estuaries, wetlands, and coastal kelp beds worldwide",
        "status": "Near Threatened to Endangered",
        "lifespan": "10 - 15 years",
        "summary": "Otters are playful, semi-aquatic carnivores famous for their streamlined bodies, webbed feet, and extraordinarily dense, water-repellent fur that traps insulating air bubbles.",
        "fun_fact": "Sea otters hold hands while resting in ocean kelp beds so they don't drift apart with the currents while sleeping.",
        "speech": "This is an Otter. Playful and clever, otters glide through rivers and oceans using streamlined bodies and webbed paws. Sea otters even hold hands while napping so ocean currents do not separate them."
    },
    "owl": {
        "scientific_name": "Strigiformes",
        "diet": "Carnivore (Mice, voles, rats, insects, fish)",
        "habitat": "Woodlands, barns, tundras, and deserts globally",
        "status": "Least Concern to Vulnerable",
        "lifespan": "10 - 25 years",
        "summary": "Owls are solitary nocturnal raptors renowned for silent flight enabled by fringed wing feathers, asymmetric ears that locate sounds in total darkness, and the ability to rotate their necks 270 degrees.",
        "fun_fact": "An owl's large eyes are tubular rather than spherical, held in place by bony eye rings, which is why they must rotate their entire heads to look around.",
        "speech": "This bird is an Owl. Owls are nocturnal hunters that glide through the darkness in total silence due to velvety feather fringes. They can rotate their heads 270 degrees to locate prey."
    },
    "ox": {
        "scientific_name": "Bos taurus",
        "diet": "Herbivore (Grasses, clover, straw)",
        "habitat": "Pastures, farmlands, and rural working communities worldwide",
        "status": "Domesticated",
        "lifespan": "15 - 20 years",
        "summary": "Oxen are domesticated draft cattle trained from an early age to pull plows, carts, and heavy agricultural loads. Known for their calm temperament and muscular stamina, they have been working partners to humans for millennia.",
        "fun_fact": "An ox can pull up to twice its own body weight over rough terrain continuously throughout a workday.",
        "speech": "This is an Ox. Oxen are muscular, domesticated draft animals celebrated for thousands of years for their calm strength, endurance, and historical role in cultivating agricultural lands."
    },
    "oyster": {
        "scientific_name": "Ostreidae",
        "diet": "Filter Feeder (Phytoplankton, marine algae)",
        "habitat": "Brackish estuaries, rocky shores, and marine ocean beds",
        "status": "Least Concern to Vulnerable",
        "lifespan": "10 - 20 years",
        "summary": "Oysters are bivalve mollusks enclosed in calcified, hinged shells. They are vital ecosystem engineers that filter ocean water and can produce shimmering natural pearls around foreign irritants.",
        "fun_fact": "A single adult oyster can filter up to 50 gallons of water per day, cleaning coastal ecosystems of excess nutrients and algae.",
        "speech": "This is an Oyster. Oysters are bivalve mollusks that serve as natural filters for oceans and estuaries, purifying up to 50 gallons of seawater every day while occasionally forming lustrous pearls."
    },
    "panda": {
        "scientific_name": "Ailuropoda melanoleuca",
        "diet": "Herbivore (Bamboo shoots and leaves make up 99%)",
        "habitat": "Bamboo-rich temperate mountain forests of southwestern China",
        "status": "Vulnerable",
        "lifespan": "20 - 30 years",
        "summary": "Giant pandas are beloved icons of wildlife conservation characterized by their bold black-and-white coats, round faces, and peaceful nature. They spend 12 hours a day munching on bamboo.",
        "fun_fact": "Pandas have an elongated wrist bone that functions like an opposable 'pseudo-thumb' to grasp thick bamboo stalks while eating.",
        "speech": "This is a Giant Panda. Loved across the globe, giant pandas spend over twelve hours a day feasting on bamboo in misty Chinese mountain forests, holding stalks using a specialized opposable thumb bone."
    },
    "parrot": {
        "scientific_name": "Psittaciformes",
        "diet": "Herbivore / Frugivore (Seeds, nuts, fruits, blossoms)",
        "habitat": "Tropical and subtropical rainforests, woodlands, and savannahs",
        "status": "Varies by species",
        "lifespan": "20 - 80 years (by species)",
        "summary": "Parrots are vibrant, charismatic birds recognized by curved beaks, zygodactyl feet (two toes forward, two back), and remarkable vocal mimicry and problem-solving intelligence.",
        "fun_fact": "African Grey parrots have demonstrated language comprehension and abstract reasoning comparable to a five-year-old child.",
        "speech": "This bird is a Parrot. Parrots are celebrated for their brilliant feathers, long lifespans, and exceptional ability to mimic human speech and understand complex cognitive puzzles."
    },
    "pelecaniformes": {
        "scientific_name": "Pelecaniformes (Pelicans, herons, ibises)",
        "diet": "Carnivore (Fish, frogs, crustaceans, aquatic insects)",
        "habitat": "Coastlines, lakes, wetlands, and estuaries globally",
        "status": "Least Concern",
        "lifespan": "15 - 25 years",
        "summary": "Pelecaniformes are medium-to-large aquatic birds with long bills and specialized throat pouches or spear-like beaks used for snatching fish from coastal waters and lagoons.",
        "fun_fact": "A pelican's expandable throat pouch can hold up to 3 gallons of water—roughly three times more than its stomach can digest at once.",
        "speech": "This bird belongs to the order Pelecaniformes, which includes pelicans and herons. These coastal birds use specialized beak pouches to scoop fish straight from the water."
    },
    "penguin": {
        "scientific_name": "Spheniscidae",
        "diet": "Carnivore (Krill, squid, small fish)",
        "habitat": "Coasts, ice sheets, and open waters of the Southern Hemisphere",
        "status": "Varies by species",
        "lifespan": "15 - 20 years",
        "summary": "Penguins are flightless marine birds dressed in natural 'tuxedos' (countershading camouflage). Their wings have evolved into rigid, hydrodynamic flippers, making them lightning-fast ocean swimmers.",
        "fun_fact": "Emperor penguins can dive to depths exceeding 500 meters and hold their breath for over 20 minutes in freezing Antarctic waters.",
        "speech": "This bird is a Penguin. Penguins are flightless aquatic birds whose wings act like flippers under water. Their black-and-white coloration provides camouflage against ocean predators."
    },
    "pig": {
        "scientific_name": "Sus domesticus",
        "diet": "Omnivore (Grains, vegetables, roots, fruits)",
        "habitat": "Farms, pastures, and woodlands worldwide",
        "status": "Domesticated",
        "lifespan": "12 - 20 years",
        "summary": "Pigs are clean, deeply intelligent farm animals that rank among the top ten smartest animals on Earth. They love to roll in mud only because they lack sweat glands and need mud to cool down and protect skin.",
        "fun_fact": "Pigs are smarter than dogs and can learn to play video games using their snouts to manipulate joysticks.",
        "speech": "This is a Pig. Pigs are remarkably smart and clean animals. Because they lack sweat glands, they bathe in cool mud to regulate body temperature and shield their skin from sunlight."
    },
    "pigeon": {
        "scientific_name": "Columba livia",
        "diet": "Herbivore / Granivore (Seeds, grains, berries, bread crumbs)",
        "habitat": "Urban squares, cliffs, and countryside worldwide",
        "status": "Least Concern",
        "lifespan": "5 - 15 years",
        "summary": "Pigeons (or rock doves) are robust, gentle birds famous for their navigation abilities. Humans have used homing pigeons for thousands of years to carry messages across battlefields and oceans.",
        "fun_fact": "Pigeons can find their way back home from over 1,000 miles away by reading the Earth's magnetic fields and the position of the sun.",
        "speech": "This bird is a Pigeon. Renowned as historical couriers, pigeons are master navigators that can return home from over a thousand miles away by sensing Earth's magnetic field."
    },
    "porcupine": {
        "scientific_name": "Hystricidae / Erethizontidae",
        "diet": "Herbivore (Leaves, twigs, tree bark, roots, nuts)",
        "habitat": "Forests, hillsides, and deserts of the Americas, Africa, and Eurasia",
        "status": "Least Concern",
        "lifespan": "10 - 18 years",
        "summary": "Porcupines are slow-moving, large rodents armed with an armor of up to 30,000 sharp, barbed quills. When cornered, they turn their back and swat with their tail, lodging quills into attackers.",
        "fun_fact": "Contrary to cartoons, porcupines cannot shoot their quills; the quills simply detach on contact and embed with backwards-pointing microscopic barbs.",
        "speech": "This is a Porcupine. Porcupines are armored herbivores shielded by tens of thousands of barbed quills that detach instantly upon touch to deter predators like cougars and leopards."
    },
    "possum": {
        "scientific_name": "Phalangeriformes / Didelphimorphia",
        "diet": "Omnivore (Insects, fruit, leaves, eggs, ticks)",
        "habitat": "Tree canopies, woodlands, and urban parks across Australasia and the Americas",
        "status": "Least Concern",
        "lifespan": "3 - 8 years",
        "summary": "Possums (and opossums) are adaptable marsupials equipped with prehensile tails and opposable hallux toes for climbing branches. American opossums are famous for feigning death ('playing possum') when terrified.",
        "fun_fact": "A single opossum can eat thousands of disease-carrying ticks in a single season, helping reduce Lyme disease in forests.",
        "speech": "This is a Possum. Marsupials with prehensile tails for climbing trees, possums are famous for playing dead when threatened and play an important ecological role by consuming thousands of ticks."
    },
    "raccoon": {
        "scientific_name": "Procyon lotor",
        "diet": "Omnivore (Fruits, nuts, insects, frogs, urban food scraps)",
        "habitat": "Forests, marshes, suburban neighborhoods, and cities",
        "status": "Least Concern",
        "lifespan": "3 - 5 years in wild",
        "summary": "Raccoons are medium-sized mammals recognizable by their black bandit facial mask and bushy ringed tail. Their front paws are extremely sensitive and nimble, allowing them to open latches and wash food.",
        "fun_fact": "A raccoon's front paws become much more tactile and sensitive when wet, which is why they often 'wash' their food in water before eating.",
        "speech": "This is a Raccoon. Famous for their bandit mask markings and ringed tails, raccoons possess nimble five-toed paws capable of opening jars, latches, and foraging through city neighborhoods."
    },
    "rat": {
        "scientific_name": "Rattus",
        "diet": "Omnivore (Grains, seeds, scraps, fruits, meat)",
        "habitat": "Urban centers, burrows, sewers, and agricultural fields worldwide",
        "status": "Least Concern",
        "lifespan": "2 - 3 years",
        "summary": "Rats are remarkably intelligent, empathetic, and adaptable rodents. They have strong teeth that never stop growing, excellent memory, and communicate through ultrasonic chirps when tickled.",
        "fun_fact": "Rats laugh when tickled and have demonstrated empathy in lab tests by freeing trapped cagemates even when reward treats were available.",
        "speech": "This is a Rat. Highly intelligent and social rodents, rats possess acute memory and problem-solving skills, and even emit ultrasonic laughter when playing and tickled."
    },
    "reindeer": {
        "scientific_name": "Rangifer tarandus",
        "diet": "Herbivore (Lichens, moss, willow leaves, fungi)",
        "habitat": "Arctic tundras and subarctic taiga forests of North America and Eurasia",
        "status": "Vulnerable",
        "lifespan": "15 - 18 years",
        "summary": "Reindeer (known as caribou in North America) are cold-adapted deer with wide, hollow hooves that act like snowshoes. Both males and females grow antlers, which they shed at different times of the year.",
        "fun_fact": "A reindeer's eyes change color from gold in summer to deep blue in dark arctic winter to capture more scattered ultraviolet light.",
        "speech": "This is a Reindeer. Specially adapted for freezing arctic tundras, reindeer have wide snowshoe hooves and eyes that shift color from gold to deep blue to navigate dark polar winters."
    },
    "rhinoceros": {
        "scientific_name": "Rhinocerotidae",
        "diet": "Herbivore (Grasses, tree foliage, branches, fruit)",
        "habitat": "Savannahs, floodplains, and tropical forests of Africa and Asia",
        "status": "Vulnerable to Critically Endangered",
        "lifespan": "35 - 50 years",
        "summary": "Rhinoceroses are prehistoric-looking armored giants weighing up to 2,500 kg. Their iconic horns are composed not of bone, but of compressed keratin—the same protein found in human hair and fingernails.",
        "fun_fact": "Despite their tank-like armor and massive weight, rhinos can sprint at speeds up to 55 km/h (34 mph).",
        "speech": "This is a Rhinoceros. Rhino species are majestic armored giants whose signature horns are made of dense keratin. Despite their size, rhinos can sprint as fast as a running racehorse."
    },
    "sandpiper": {
        "scientific_name": "Scolopacidae",
        "diet": "Carnivore / Invertivore (Tiny crabs, worms, marine mollusks)",
        "habitat": "Sandy beaches, mudflats, and shorelines worldwide",
        "status": "Least Concern",
        "lifespan": "5 - 10 years",
        "summary": "Sandpipers are slender shorebirds with long legs and sensitive bills. They scurry along wave lines on beaches, rapidly probing the wet sand to pluck out buried worms, amphipods, and miniature crustaceans.",
        "fun_fact": "The tips of sandpiper bills are filled with nerve receptors that can detect vibrations of underground prey without even seeing them.",
        "speech": "This bird is a Sandpiper. Sandpipers are agile coastal birds that dash back and forth with incoming ocean surf, using probe-like beaks to snatch invertebrates hidden in damp sand."
    },
    "seahorse": {
        "scientific_name": "Hippocampus",
        "diet": "Carnivore (Tiny crustaceans, brine shrimp, plankton)",
        "habitat": "Shallow coastal waters, seagrass beds, and coral reefs",
        "status": "Vulnerable",
        "lifespan": "1 - 5 years",
        "summary": "Seahorses are unique bony fish with horse-like heads, prehensile monkey-like tails, and no stomach. They swim upright and anchor themselves to seagrass blades to avoid being swept away by currents.",
        "fun_fact": "Seahorses are the only animal species on Earth where the male experiences pregnancy and gives birth to hundreds of babies from his brood pouch.",
        "speech": "This is a Seahorse. Swimming vertically among coral reefs and seagrass, seahorses anchor themselves with curled tails. Uniquely in the animal kingdom, male seahorses carry eggs and give birth to young."
    },
    "seal": {
        "scientific_name": "Pinnipedia",
        "diet": "Carnivore (Fish, squid, crustaceans, krill)",
        "habitat": "Polar and temperate ocean coasts, ice floes, and open waters",
        "status": "Least Concern to Endangered",
        "lifespan": "20 - 30 years",
        "summary": "Seals are streamlined, blubbery marine carnivores with fin-like flippers. They spend months foraging in open seas and haul out onto sandy beaches or pack ice to rest, molt, and give birth to pups.",
        "fun_fact": "Seals have blood that contains higher concentrations of hemoglobin than humans, allowing them to dive for over an hour without breathing.",
        "speech": "This is a Seal. Seals are agile ocean predators with insulating layers of blubber and sensitive whiskers that track fish in murky seas, coming ashore onto rocky coasts and ice floes to rest."
    },
    "shark": {
        "scientific_name": "Selachimorpha",
        "diet": "Carnivore (Fish, seals, squid, crustaceans, plankton)",
        "habitat": "Every ocean basin on Earth, from shallow reefs to the deep abyss",
        "status": "Vulnerable to Critically Endangered",
        "lifespan": "20 - 100+ years (Greenland sharks up to 400 years)",
        "summary": "Sharks are ancient cartilaginous apex predators that have patrolled the oceans for over 400 million years. They have multiple rows of replaceable teeth and electroreceptive organs called Ampullae of Lorenzini.",
        "fun_fact": "Sharks can detect a single drop of blood diluted across an Olympic-sized swimming pool and sense the electrical heartbeat of buried fish.",
        "speech": "This is a Shark. Ancient apex guardians of the seas, sharks possess skeletons made of flexible cartilage and specialized electroreceptors that detect the faint heartbeats of prey buried in ocean sand."
    },
    "sheep": {
        "scientific_name": "Ovis aries",
        "diet": "Herbivore (Grasses, legumes, clover)",
        "habitat": "Pastures, grasslands, and hillsides globally",
        "status": "Domesticated",
        "lifespan": "10 - 15 years",
        "summary": "Sheep are gentle, wool-producing ruminants domesticated over 10,000 years ago. Highly social herd animals, they possess exceptional spatial recognition, recognizing human and sheep faces for years.",
        "fun_fact": "Sheep have specialized rectangular pupils that allow them to see behind themselves without turning their heads.",
        "speech": "This is a Sheep. Domesticated for thousands of years for wool and milk, sheep are social herd grazers that possess wide-angle peripheral vision and can remember dozens of individual faces."
    },
    "snake": {
        "scientific_name": "Serpentes",
        "diet": "Carnivore (Rodents, birds, eggs, frogs, insects)",
        "habitat": "Tropical forests, savannahs, deserts, and swamps on every continent except Antarctica",
        "status": "Varies by species",
        "lifespan": "10 - 25 years",
        "summary": "Snakes are elongated, limbless carnivores covered in smooth scales. They 'smell' the air using their forked tongues and Jacobson's organ, and unhinge their flexible jaws to swallow prey larger than their heads.",
        "fun_fact": "A snake's lower jaw is connected by stretchy ligaments, allowing it to open its mouth up to 150 degrees to ingest meals whole.",
        "speech": "This is a Snake. Limbless and graceful, snakes track scents through the air with their forked tongues and can unhinge flexible jaw ligaments to swallow meals substantially larger than their head."
    },
    "sparrow": {
        "scientific_name": "Passeridae",
        "diet": "Omnivore / Granivore (Seeds, grains, berries, small insects)",
        "habitat": "Cities, gardens, farms, and hedgerows worldwide",
        "status": "Least Concern",
        "lifespan": "3 - 5 years",
        "summary": "Sparrows are small, cheerful brown songbirds common in urban and rural environments. Their conical, stout beaks are expertly crafted for cracking hard seeds and grains.",
        "fun_fact": "House sparrows frequently engage in communal dust baths, throwing dirt over their feathers to clean plumage and dislodge tiny parasites.",
        "speech": "This bird is a Sparrow. Friendly and ubiquitous songbirds, sparrows sport sturdy seed-cracking beaks and cheerful chirps, frequently nesting near human dwellings and gardens."
    },
    "squid": {
        "scientific_name": "Teuthida",
        "diet": "Carnivore (Fish, crustaceans, other squid)",
        "habitat": "Open oceans and deep twilight ocean trenches worldwide",
        "status": "Least Concern",
        "lifespan": "1 - 3 years",
        "summary": "Squid are swift, hydrodynamic cephalopods equipped with eight arms, two elongated feeding tentacles, and a siphon that shoots water for jet propulsion. Giant squid in deep ocean trenches can reach 13 meters.",
        "fun_fact": "Squid have the largest eyes in the animal kingdom; a giant squid's eye can be the size of a dinner plate.",
        "speech": "This is a Squid. Jetting through ocean depths using water siphons, squid possess eight arms and two capture tentacles, alongside the largest eyes in the entire animal kingdom."
    },
    "squirrel": {
        "scientific_name": "Sciuridae",
        "diet": "Omnivore (Acorns, pine cones, nuts, berries, bird eggs)",
        "habitat": "Woodlands, city parks, and suburbs across the globe",
        "status": "Least Concern",
        "lifespan": "5 - 10 years",
        "summary": "Squirrels are acrobatic, bushy-tailed rodents known for their tree-climbing agility and habit of burying nuts across woodlands, accidentally planting millions of new oak and walnut trees every year.",
        "fun_fact": "Squirrels accidentally plant millions of trees each year because they forget the exact location of up to 74% of the nuts they bury.",
        "speech": "This is a Squirrel. Agile acrobats of the forest canopy, squirrels bury thousands of acorns every autumn, unintentionally acting as nature's greatest forest planters when they forget where they hid them."
    },
    "starfish": {
        "scientific_name": "Asteroidea",
        "diet": "Carnivore (Clams, oysters, mussels, snails)",
        "habitat": "Seabeds, coral reefs, and coastal tidal rock pools",
        "status": "Least Concern",
        "lifespan": "10 - 35 years",
        "summary": "Starfish (sea stars) are marine invertebrates typically with five radiating arms covered in hundreds of suction-cup tube feet. They have no brain or blood, circulating filtered seawater through their bodies instead.",
        "fun_fact": "A sea star can push its entire stomach out of its mouth into a clam's shell to digest the prey externally before slurping it back in.",
        "speech": "This is a Starfish. Found clinging to rocky tide pools, starfish circulate seawater instead of blood and can regenerate lost arms—and even an entire body—from a single severed limb."
    },
    "swan": {
        "scientific_name": "Cygnus",
        "diet": "Herbivore (Aquatic plants, pond weed, tubers, seeds)",
        "habitat": "Lakes, ponds, tranquil rivers, and coastal wetlands",
        "status": "Least Concern",
        "lifespan": "20 - 30 years",
        "summary": "Swans are large, elegant waterfowl famous for their pristine white plumage, graceful S-shaped necks, and romantic lifelong pair bonds. Despite their poise, they will aggressively defend their nests from intruders.",
        "fun_fact": "Swans form monogamous bonds that typically last for life, and pairs often swim with their necks aligned to form a heart shape.",
        "speech": "This bird is a Swan. Celebrated as symbols of beauty and fidelity, swans glide gracefully across tranquil lakes, forming lifelong pairs and fiercely defending their cygnets."
    },
    "tiger": {
        "scientific_name": "Panthera tigris",
        "diet": "Carnivore (Deer, wild boar, buffalo, antelopes)",
        "habitat": "Tropical rainforests, evergreen forests, mangrove swamps, and grasslands across Asia",
        "status": "Endangered",
        "lifespan": "10 - 15 years in wild",
        "summary": "Tigers are the largest wild feline species in the world. As solitary apex predators, they are distinguished by their reddish-orange coats with dark vertical stripes that camouflage them in tall grasses and jungle shade.",
        "fun_fact": "No two tigers have the exact same stripe pattern; each tiger's coat is unique, and the stripes are pigmented directly into their skin, not just the fur.",
        "speech": "This animal is a Tiger. Tigers are the largest wild cats on Earth, recognized by their iconic orange coats and dark vertical stripes. Every tiger's stripe pattern is completely unique, like human fingerprints, and they are excellent swimmers that love bathing in forest pools."
    },
    "turkey": {
        "scientific_name": "Meleagris gallopavo",
        "diet": "Omnivore (Acorns, seeds, berries, insects, small lizards)",
        "habitat": "Hardwood forests and woodlands of North America",
        "status": "Least Concern",
        "lifespan": "3 - 5 years in wild",
        "summary": "Turkeys are large game birds native to North America. Males (toms) are famous for fanning their iridescent tail feathers and displaying fleshy neck wattles and snoods that change color based on emotion.",
        "fun_fact": "A wild turkey can fly in short bursts at speeds up to 55 mph (88 km/h) and sprint on foot at 20 mph.",
        "speech": "This bird is a Turkey. Native to North American woodlands, wild turkeys can run over twenty miles per hour and display iridescent tail fans and colorful neck wattles to attract mates."
    },
    "turtle": {
        "scientific_name": "Testudines",
        "diet": "Omnivore / Herbivore (Jellyfish, sea grasses, algae, worms)",
        "habitat": "Oceans, freshwater lakes, ponds, and riverbanks globally",
        "status": "Vulnerable to Critically Endangered",
        "lifespan": "40 - 100+ years",
        "summary": "Turtles are ancient reptiles encased in a bony or cartilaginous shell composed of a carapace on top and plastron below. Sea turtles navigate across entire ocean basins using Earth's magnetic fields.",
        "fun_fact": "A turtle's shell is not an external suit of armor—it is part of its actual skeleton, fused directly to its spine and ribcage.",
        "speech": "This is a Turtle. Ancient reptiles with shells fused directly to their ribcages, turtles have sailed Earth's oceans and rivers for over two hundred million years, with sea turtles navigating across oceans back to their birth beaches."
    },
    "whale": {
        "scientific_name": "Cetacea",
        "diet": "Carnivore / Filter Feeder (Krill, plankton, small fish, squid)",
        "habitat": "All ocean basins, from arctic seas to warm equatorial waters",
        "status": "Vulnerable to Endangered (by species)",
        "lifespan": "50 - 100+ years (Bowhead whales up to 200 years)",
        "summary": "Whales are colossal, air-breathing marine mammals. The Blue Whale is the largest animal ever known to have lived on Earth, reaching lengths over 30 meters and weights exceeding 150 metric tons.",
        "fun_fact": "A blue whale's heart is the size of a small car, and its heartbeat can be detected from over two miles away underwater.",
        "speech": "This is a Whale. Whales are the majestic leviathans of the sea. The Blue Whale is the largest creature ever to inhabit planet Earth, whose haunting underwater songs travel across thousands of miles of open ocean."
    },
    "wolf": {
        "scientific_name": "Canis lupus",
        "diet": "Carnivore (Elk, deer, moose, bison, small mammals)",
        "habitat": "Forests, tundras, grasslands, and mountains of the Northern Hemisphere",
        "status": "Least Concern",
        "lifespan": "6 - 8 years in wild",
        "summary": "Wolves are legendary wild canines that live in cohesive family packs led by an alpha pair. They communicate across vast wildernesses using expressive body language, scent marking, and soulful collective howls.",
        "fun_fact": "A wolf's howl carries over 16 kilometers (10 miles) in open wilderness, serving to coordinate pack movements and deter rival packs.",
        "speech": "This is a Wolf. Wolves are legendary pack hunters renowned for cooperative teamwork, endurance running, and evocative howls that echo across miles of mountain wilderness."
    },
    "wombat": {
        "scientific_name": "Vombatidae",
        "diet": "Herbivore (Grasses, sedges, roots, tree bark)",
        "habitat": "Forested, mountainous, and heathland areas of south-eastern Australia",
        "status": "Least Concern to Critically Endangered",
        "lifespan": "15 - 20 years",
        "summary": "Wombats are short-legged, muscular burrowing marsupials native to Australia. They possess a backwards-facing pouch so dirt doesn't enter while digging and produce distinctive cube-shaped droppings.",
        "fun_fact": "Wombats are the only animals in the world that produce cube-shaped poop, which prevents their territorial markers from rolling off rocks!",
        "speech": "This is a Wombat. Wombats are sturdy, burrowing Australian marsupials with backwards-facing pouches to keep their young free of dirt, and they are famously the only creatures to produce cube-shaped droppings."
    },
    "woodpecker": {
        "scientific_name": "Picidae",
        "diet": "Insectivore (Tree-boring beetle larvae, ants, sap, nuts)",
        "habitat": "Forests, woodlands, and groves worldwide except Australasia",
        "status": "Least Concern",
        "lifespan": "4 - 12 years",
        "summary": "Woodpeckers are specialized birds famous for pecking into tree trunks with chisel-shaped beaks to find insects and excavate nest cavities. Their tongues wrap completely around their skulls to cushion their brains.",
        "fun_fact": "A woodpecker pecks tree trunks up to 20 times per second, experiencing up to 1,200 Gs of deceleration—safeguarded by a shock-absorbing skull and hyoid bone.",
        "speech": "This bird is a Woodpecker. Woodpeckers drum into tree trunks at twenty pecks per second. Their long tongues wrap around their skulls to serve as biological shock absorbers, shielding their brains from high-impact vibrations."
    },
    "zebra": {
        "scientific_name": "Equus quagga / Equus zebra",
        "diet": "Herbivore (Coarse grasses, shrubs, herbs)",
        "habitat": "Treeless grasslands and savannah woodlands of eastern and southern Africa",
        "status": "Near Threatened",
        "lifespan": "20 - 25 years",
        "summary": "Zebras are iconic African equines famous for their dazzling black-and-white striped coats. These stripes confuse biting flies, dissipate savannah heat through convection currents, and create optical illusions that dazzle predators.",
        "fun_fact": "Zebras are actually black with white stripes; in early embryonic development they are completely black, developing white stripes before birth.",
        "speech": "This is a Zebra. Famous for their striking monochrome stripes, zebras roam African savannahs in family harems. Their stripes disrupt thermal heat waves, deter biting insects, and confuse stalking predators like lions."
    }
}


def get_animal_info(animal_name):
    key = str(animal_name).strip().lower()
    if key in ANIMAL_INFO:
        return ANIMAL_INFO[key]
    
    # Generic fallback if key not found
    return {
        "scientific_name": f"Species: {animal_name.title()}",
        "diet": "Wild animal diet",
        "habitat": "Natural habitat",
        "status": "Monitored species",
        "lifespan": "Varies by species",
        "summary": f"{animal_name.title()} is one of the 90 species represented in the wildlife dataset. It possesses specialized physical adaptations suited to its natural environment.",
        "fun_fact": f"The {animal_name.title()} plays an integral role in maintaining the balance of its native ecological food web.",
        "speech": f"This image is predicted as a {animal_name.title()}. It is one of the ninety animal species recognized by this EfficientNetB3 deep learning model."
    }
