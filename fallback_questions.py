# fallback_questions.py
# -------------------------------------------------------------------
# Offline fallback question bank used when the API is unavailable.
# Each question is a dict with:
#   prompt       – the question text
#   choices      – list of exactly 4 answer strings
#   answer_index – 0-based index of the CORRECT answer inside choices
#   category     – must match the API category name exactly (see list below)
#   difficulty   – "Easy" | "Medium" | "Hard"
#
# Category names used by OpenTDB API:
#   "General Knowledge"
#   "Science: Computers"
#   "Sports"
#   "Geography"
#   "History"
#   "Science & Nature"
#   "Entertainment: Books"
#   "Entertainment: Film"
#   "Entertainment: Music"
#   "Entertainment: Video Games"
#   "Mythology"
#   "Animals"
#   "Politics"
#   "Entertainment: Comics"
# -------------------------------------------------------------------

FALLBACK_QUESTIONS = [

    # ════════════════════════════════════════════════════════════
    #  GENERAL KNOWLEDGE
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "Which is the largest ocean on Earth?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer_index": 3,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many continents are there on Earth?",
        "choices": ["5", "6", "7", "8"],
        "answer_index": 2,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the currency of Japan?",
        "choices": ["Yuan", "Won", "Yen", "Ringgit"],
        "answer_index": 2,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Jupiter", "Saturn", "Mars"],
        "answer_index": 3,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many sides does a hexagon have?",
        "choices": ["5", "7", "6", "8"],
        "answer_index": 2,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the smallest country in the world?",
        "choices": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"],
        "answer_index": 2,
        "category": "General Knowledge",
        "difficulty": "Medium"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "choices": ["Michelangelo", "Raphael", "Donatello", "Leonardo da Vinci"],
        "answer_index": 3,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the chemical symbol for gold?",
        "choices": ["Go", "Gd", "Gl", "Au"],
        "answer_index": 3,
        "category": "General Knowledge",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which country is home to the kangaroo?",
        "choices": ["New Zealand", "South Africa", "Brazil", "Australia"],
        "answer_index": 3,
        "category": "General Knowledge",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many bones are in the adult human body?",
        "choices": ["196", "206", "216", "226"],
        "answer_index": 1,
        "category": "General Knowledge",
        "difficulty": "Medium"
    },

    # ════════════════════════════════════════════════════════════
    #  SCIENCE: COMPUTERS
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "What does CPU stand for?",
        "choices": ["Central Processing Unit", "Central Program Unit", "Core Processing Unit", "Computer Personal Unit"],
        "answer_index": 0,
        "category": "Science: Computers",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which language is known as the backbone of the web?",
        "choices": ["Python", "Java", "HTML", "C++"],
        "answer_index": 2,
        "category": "Science: Computers",
        "difficulty": "Easy"
    },
    {
        "prompt": "What does RAM stand for?",
        "choices": ["Random Access Memory", "Read Access Memory", "Rapid Access Memory", "Remote Access Module"],
        "answer_index": 0,
        "category": "Science: Computers",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which company created the Python programming language?",
        "choices": ["Microsoft", "Google", "It was created by Guido van Rossum, not a company", "Apple"],
        "answer_index": 2,
        "category": "Science: Computers",
        "difficulty": "Medium"
    },
    {
        "prompt": "What does 'HTTP' stand for?",
        "choices": ["HyperText Transfer Protocol", "High Transfer Text Protocol", "HyperText Transmission Program", "Hyper Transfer Text Procedure"],
        "answer_index": 0,
        "category": "Science: Computers",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which data structure operates on a LIFO principle?",
        "choices": ["Queue", "Array", "Stack", "Linked List"],
        "answer_index": 2,
        "category": "Science: Computers",
        "difficulty": "Medium"
    },
    {
        "prompt": "What is the binary representation of the decimal number 10?",
        "choices": ["1010", "1001", "1100", "0110"],
        "answer_index": 0,
        "category": "Science: Computers",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which of the following is NOT an operating system?",
        "choices": ["Linux", "Windows", "Oracle", "macOS"],
        "answer_index": 2,
        "category": "Science: Computers",
        "difficulty": "Easy"
    },
    {
        "prompt": "What does SQL stand for?",
        "choices": ["Simple Query Language", "Structured Query Language", "Standard Query Logic", "System Query Language"],
        "answer_index": 1,
        "category": "Science: Computers",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which port does HTTPS use by default?",
        "choices": ["80", "21", "443", "8080"],
        "answer_index": 2,
        "category": "Science: Computers",
        "difficulty": "Hard"
    },

    # ════════════════════════════════════════════════════════════
    #  SPORTS
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "How many players are on a standard football (soccer) team on the field?",
        "choices": ["9", "10", "11", "12"],
        "answer_index": 2,
        "category": "Sports",
        "difficulty": "Easy"
    },
    {
        "prompt": "In which sport is the term 'love' used to mean zero?",
        "choices": ["Badminton", "Table Tennis", "Squash", "Tennis"],
        "answer_index": 3,
        "category": "Sports",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many rings are on the Olympic flag?",
        "choices": ["4", "5", "6", "7"],
        "answer_index": 1,
        "category": "Sports",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which country won the first FIFA World Cup in 1930?",
        "choices": ["Brazil", "Argentina", "Uruguay", "Italy"],
        "answer_index": 2,
        "category": "Sports",
        "difficulty": "Hard"
    },
    {
        "prompt": "In basketball, how many points is a free throw worth?",
        "choices": ["2", "3", "1", "4"],
        "answer_index": 2,
        "category": "Sports",
        "difficulty": "Easy"
    },
    {
        "prompt": "How long is a marathon race in kilometers (approx)?",
        "choices": ["40 km", "42.195 km", "45 km", "38 km"],
        "answer_index": 1,
        "category": "Sports",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which sport uses a shuttlecock?",
        "choices": ["Squash", "Racquetball", "Badminton", "Paddle Tennis"],
        "answer_index": 2,
        "category": "Sports",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many players are on a standard cricket team?",
        "choices": ["9", "10", "12", "11"],
        "answer_index": 3,
        "category": "Sports",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which Grand Slam tennis tournament is played on clay?",
        "choices": ["Wimbledon", "US Open", "Australian Open", "French Open"],
        "answer_index": 3,
        "category": "Sports",
        "difficulty": "Medium"
    },
    {
        "prompt": "In which year were the first modern Olympic Games held?",
        "choices": ["1892", "1896", "1900", "1888"],
        "answer_index": 1,
        "category": "Sports",
        "difficulty": "Medium"
    },

    # ════════════════════════════════════════════════════════════
    #  GEOGRAPHY
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "What is the capital of Australia?",
        "choices": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which is the longest river in the world?",
        "choices": ["Amazon", "Yangtze", "Mississippi", "Nile"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which country has the most natural lakes?",
        "choices": ["Russia", "United States", "Canada", "Finland"],
        "answer_index": 2,
        "category": "Geography",
        "difficulty": "Hard"
    },
    {
        "prompt": "Mount Everest is located on the border of which two countries?",
        "choices": ["India and Tibet", "Nepal and Tibet", "Nepal and India", "Bhutan and China"],
        "answer_index": 1,
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "prompt": "What is the capital of Canada?",
        "choices": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which desert is the largest in the world?",
        "choices": ["Gobi", "Sahara", "Arabian", "Antarctic"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Hard"
    },
    {
        "prompt": "Which country is both an island and a continent?",
        "choices": ["New Zealand", "Greenland", "Australia", "Madagascar"],
        "answer_index": 2,
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "prompt": "The Amazon rainforest is primarily located in which country?",
        "choices": ["Colombia", "Venezuela", "Peru", "Brazil"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the capital of Brazil?",
        "choices": ["Rio de Janeiro", "Sao Paulo", "Salvador", "Brasilia"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which ocean lies between Europe and North America?",
        "choices": ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"],
        "answer_index": 3,
        "category": "Geography",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  HISTORY
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "In which year did World War II end?",
        "choices": ["1943", "1944", "1946", "1945"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Easy"
    },
    {
        "prompt": "Who was the first President of the United States?",
        "choices": ["John Adams", "Thomas Jefferson", "Benjamin Franklin", "George Washington"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Easy"
    },
    {
        "prompt": "The Berlin Wall fell in which year?",
        "choices": ["1987", "1990", "1991", "1989"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which empire was ruled by Julius Caesar?",
        "choices": ["Greek Empire", "Ottoman Empire", "Persian Empire", "Roman Empire"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Easy"
    },
    {
        "prompt": "In which year did India gain independence from British rule?",
        "choices": ["1945", "1948", "1950", "1947"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Easy"
    },
    {
        "prompt": "Who was the first man to walk on the Moon?",
        "choices": ["Buzz Aldrin", "Yuri Gagarin", "John Glenn", "Neil Armstrong"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Easy"
    },
    {
        "prompt": "The French Revolution began in which year?",
        "choices": ["1776", "1803", "1815", "1789"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which ancient wonder was located in Alexandria, Egypt?",
        "choices": ["Colossus of Rhodes", "Statue of Zeus", "Temple of Artemis", "Lighthouse of Alexandria"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Hard"
    },
    {
        "prompt": "Who wrote the Communist Manifesto?",
        "choices": ["Vladimir Lenin", "Friedrich Engels and Karl Marx", "Leon Trotsky", "Joseph Stalin"],
        "answer_index": 1,
        "category": "History",
        "difficulty": "Medium"
    },
    {
        "prompt": "What was the name of the ship that sank in 1912 after hitting an iceberg?",
        "choices": ["Britannic", "Olympic", "Lusitania", "Titanic"],
        "answer_index": 3,
        "category": "History",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  SCIENCE & NATURE
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "What is the chemical symbol for water?",
        "choices": ["WA", "HO2", "OW", "H2O"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many elements are in the periodic table (as of 2024)?",
        "choices": ["112", "116", "120", "118"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Medium"
    },
    {
        "prompt": "What is the powerhouse of the cell?",
        "choices": ["Nucleus", "Ribosome", "Golgi Apparatus", "Mitochondria"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Easy"
    },
    {
        "prompt": "What planet is closest to the Sun?",
        "choices": ["Venus", "Earth", "Mars", "Mercury"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the speed of light in a vacuum (approx)?",
        "choices": ["200,000 km/s", "250,000 km/s", "350,000 km/s", "300,000 km/s"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Medium"
    },
    {
        "prompt": "What gas do plants absorb during photosynthesis?",
        "choices": ["Oxygen", "Nitrogen", "Hydrogen", "Carbon Dioxide"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many chromosomes does a normal human cell contain?",
        "choices": ["23", "36", "92", "46"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Medium"
    },
    {
        "prompt": "What is the most abundant gas in Earth's atmosphere?",
        "choices": ["Oxygen", "Carbon Dioxide", "Argon", "Nitrogen"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which scientist formulated the theory of general relativity?",
        "choices": ["Isaac Newton", "Niels Bohr", "Stephen Hawking", "Albert Einstein"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the atomic number of carbon?",
        "choices": ["8", "10", "4", "6"],
        "answer_index": 3,
        "category": "Science & Nature",
        "difficulty": "Medium"
    },

    # ════════════════════════════════════════════════════════════
    #  ENTERTAINMENT: BOOKS
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "Who wrote 'Harry Potter and the Philosopher's Stone'?",
        "choices": ["Tolkien", "C.S. Lewis", "Roald Dahl", "J.K. Rowling"],
        "answer_index": 3,
        "category": "Entertainment: Books",
        "difficulty": "Easy"
    },
    {
        "prompt": "In which novel would you find the character Sherlock Holmes?",
        "choices": ["The Adventures of Hercule Poirot", "The Maltese Falcon", "A Study in Scarlet", "And Then There Were None"],
        "answer_index": 2,
        "category": "Entertainment: Books",
        "difficulty": "Easy"
    },
    {
        "prompt": "Who wrote '1984'?",
        "choices": ["Aldous Huxley", "Ray Bradbury", "H.G. Wells", "George Orwell"],
        "answer_index": 3,
        "category": "Entertainment: Books",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the first book of the Bible?",
        "choices": ["Exodus", "Psalms", "Leviticus", "Genesis"],
        "answer_index": 3,
        "category": "Entertainment: Books",
        "difficulty": "Easy"
    },
    {
        "prompt": "Who wrote 'Pride and Prejudice'?",
        "choices": ["Charlotte Bronte", "Emily Bronte", "Mary Shelley", "Jane Austen"],
        "answer_index": 3,
        "category": "Entertainment: Books",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  ENTERTAINMENT: FILM
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "Which film features the quote 'To infinity and beyond!'?",
        "choices": ["A Bug's Life", "Cars", "Finding Nemo", "Toy Story"],
        "answer_index": 3,
        "category": "Entertainment: Film",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which actor played Iron Man in the Marvel Cinematic Universe?",
        "choices": ["Chris Evans", "Chris Hemsworth", "Mark Ruffalo", "Robert Downey Jr."],
        "answer_index": 3,
        "category": "Entertainment: Film",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which film won the first Academy Award for Best Picture in 1928?",
        "choices": ["The Jazz Singer", "Metropolis", "Sunrise", "Wings"],
        "answer_index": 3,
        "category": "Entertainment: Film",
        "difficulty": "Hard"
    },
    {
        "prompt": "Who directed the film 'Jurassic Park' (1993)?",
        "choices": ["James Cameron", "George Lucas", "Ridley Scott", "Steven Spielberg"],
        "answer_index": 3,
        "category": "Entertainment: Film",
        "difficulty": "Medium"
    },
    {
        "prompt": "In the film 'The Matrix', what colour pill does Neo take?",
        "choices": ["Blue", "Green", "White", "Red"],
        "answer_index": 3,
        "category": "Entertainment: Film",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  ENTERTAINMENT: MUSIC
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "Which band performed 'Bohemian Rhapsody'?",
        "choices": ["Led Zeppelin", "The Rolling Stones", "The Beatles", "Queen"],
        "answer_index": 3,
        "category": "Entertainment: Music",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many strings does a standard guitar have?",
        "choices": ["4", "5", "7", "6"],
        "answer_index": 3,
        "category": "Entertainment: Music",
        "difficulty": "Easy"
    },
    {
        "prompt": "Who is known as the 'King of Pop'?",
        "choices": ["Elvis Presley", "Prince", "David Bowie", "Michael Jackson"],
        "answer_index": 3,
        "category": "Entertainment: Music",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which country does the music genre 'K-pop' originate from?",
        "choices": ["Japan", "China", "Thailand", "South Korea"],
        "answer_index": 3,
        "category": "Entertainment: Music",
        "difficulty": "Easy"
    },
    {
        "prompt": "What instrument does a pianist play?",
        "choices": ["Violin", "Cello", "Harp", "Piano"],
        "answer_index": 3,
        "category": "Entertainment: Music",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  ENTERTAINMENT: VIDEO GAMES
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "Which company created the Mario franchise?",
        "choices": ["Sega", "Atari", "Sony", "Nintendo"],
        "answer_index": 3,
        "category": "Entertainment: Video Games",
        "difficulty": "Easy"
    },
    {
        "prompt": "In the game 'Minecraft', what is the rarest ore?",
        "choices": ["Gold", "Diamond", "Redstone", "Ancient Debris (Netherite)"],
        "answer_index": 3,
        "category": "Entertainment: Video Games",
        "difficulty": "Medium"
    },
    {
        "prompt": "What is the best-selling video game of all time (standalone)?",
        "choices": ["Tetris", "Grand Theft Auto V", "The Sims", "Minecraft"],
        "answer_index": 3,
        "category": "Entertainment: Video Games",
        "difficulty": "Medium"
    },
    {
        "prompt": "In 'The Legend of Zelda', what is the name of the hero?",
        "choices": ["Ganon", "Zelda", "Epona", "Link"],
        "answer_index": 3,
        "category": "Entertainment: Video Games",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which game features the character 'Master Chief'?",
        "choices": ["Gears of War", "Call of Duty", "Destiny", "Halo"],
        "answer_index": 3,
        "category": "Entertainment: Video Games",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  MYTHOLOGY
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "Who is the Greek god of the sea?",
        "choices": ["Zeus", "Ares", "Hades", "Poseidon"],
        "answer_index": 3,
        "category": "Mythology",
        "difficulty": "Easy"
    },
    {
        "prompt": "In Norse mythology, what is the name of the world tree?",
        "choices": ["Bifrost", "Asgard", "Midgard", "Yggdrasil"],
        "answer_index": 3,
        "category": "Mythology",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which creature in Greek mythology had the head of a bull and the body of a man?",
        "choices": ["Centaur", "Sphinx", "Cyclops", "Minotaur"],
        "answer_index": 3,
        "category": "Mythology",
        "difficulty": "Easy"
    },
    {
        "prompt": "Who was the Roman equivalent of the Greek god Ares?",
        "choices": ["Jupiter", "Neptune", "Vulcan", "Mars"],
        "answer_index": 3,
        "category": "Mythology",
        "difficulty": "Medium"
    },
    {
        "prompt": "In Egyptian mythology, who is the god of the dead?",
        "choices": ["Ra", "Horus", "Anubis", "Osiris"],
        "answer_index": 3,
        "category": "Mythology",
        "difficulty": "Medium"
    },

    # ════════════════════════════════════════════════════════════
    #  ANIMALS
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "What is the largest land animal on Earth?",
        "choices": ["Giraffe", "Hippopotamus", "White Rhinoceros", "African Elephant"],
        "answer_index": 3,
        "category": "Animals",
        "difficulty": "Easy"
    },
    {
        "prompt": "How many legs does a spider have?",
        "choices": ["6", "10", "12", "8"],
        "answer_index": 3,
        "category": "Animals",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the fastest land animal?",
        "choices": ["Lion", "Pronghorn", "Greyhound", "Cheetah"],
        "answer_index": 3,
        "category": "Animals",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which bird is known for its inability to fly and its tuxedo-like appearance?",
        "choices": ["Ostrich", "Emu", "Kiwi", "Penguin"],
        "answer_index": 3,
        "category": "Animals",
        "difficulty": "Easy"
    },
    {
        "prompt": "What do you call a group of lions?",
        "choices": ["Pack", "Herd", "Colony", "Pride"],
        "answer_index": 3,
        "category": "Animals",
        "difficulty": "Easy"
    },

    # ════════════════════════════════════════════════════════════
    #  POLITICS
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "How many permanent members does the UN Security Council have?",
        "choices": ["3", "7", "10", "5"],
        "answer_index": 3,
        "category": "Politics",
        "difficulty": "Medium"
    },
    {
        "prompt": "What does 'NATO' stand for?",
        "choices": ["North Atlantic Treaty Organization", "National Alliance of Treaty Operations", "Northern Army Treaty Order", "National Atlantic Treaty Organization"],
        "answer_index": 0,
        "category": "Politics",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which document is considered the supreme law of the United States?",
        "choices": ["Declaration of Independence", "The Bill of Rights", "Articles of Confederation", "The Constitution"],
        "answer_index": 3,
        "category": "Politics",
        "difficulty": "Easy"
    },
    {
        "prompt": "In a democracy, what does the term 'suffrage' refer to?",
        "choices": ["Freedom of speech", "Right to protest", "Freedom of the press", "Right to vote"],
        "answer_index": 3,
        "category": "Politics",
        "difficulty": "Medium"
    },
    {
        "prompt": "Which international organisation promotes free trade and handles trade disputes between nations?",
        "choices": ["IMF", "World Bank", "United Nations", "WTO"],
        "answer_index": 3,
        "category": "Politics",
        "difficulty": "Medium"
    },

    # ════════════════════════════════════════════════════════════
    #  ENTERTAINMENT: COMICS
    # ════════════════════════════════════════════════════════════
    {
        "prompt": "What is the real name of Batman?",
        "choices": ["Clark Kent", "Peter Parker", "Barry Allen", "Bruce Wayne"],
        "answer_index": 3,
        "category": "Entertainment: Comics",
        "difficulty": "Easy"
    },
    {
        "prompt": "Which superhero is known as the 'Man of Steel'?",
        "choices": ["Iron Man", "Thor", "Captain America", "Superman"],
        "answer_index": 3,
        "category": "Entertainment: Comics",
        "difficulty": "Easy"
    },
    {
        "prompt": "What radioactive spider gave Peter Parker his powers?",
        "choices": ["A genetically modified black widow", "A radioactive brown recluse", "A radioactive jumping spider", "A radioactive common house spider"],
        "answer_index": 0,
        "category": "Entertainment: Comics",
        "difficulty": "Hard"
    },
    {
        "prompt": "In which city does Batman operate?",
        "choices": ["Metropolis", "Star City", "Central City", "Gotham City"],
        "answer_index": 3,
        "category": "Entertainment: Comics",
        "difficulty": "Easy"
    },
    {
        "prompt": "What is the name of Thor's hammer?",
        "choices": ["Gungnir", "Excalibur", "Gram", "Mjolnir"],
        "answer_index": 3,
        "category": "Entertainment: Comics",
        "difficulty": "Easy"
    },
]
