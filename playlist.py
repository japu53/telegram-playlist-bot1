from telethon import TelegramClient, events
import asyncio

# Put your API details here
api_id = 21435734  # Replace this with your api_id
api_hash = "50602c02f9f531b703b21d3c9765820f"  # Replace this with your api_hash

# Initialize the Telegram bot
bot = TelegramClient("playlist_bot", api_id, api_hash)

# Define song lists (to be populated later)
romantic_songs = [
    "/play Tum Hi Ho",
    "/play Tera Ban Jaunga",
    "/play Raabta",
    "/play Gerua",
    "/play Janam Janam",
    "/play Tum Mile",
    "/play Pehli Nazar Mein",
    "/play Tum Se Hi",
    "/play Tera Hone Laga Hoon",
    "/play Tujh Mein Rab Dikhta Hai",
    "/play Khuda Jaane",
    "/play Sun Saathiya",
    "/play Sanam Re",
    "/play Phir Kabhi",
    "/play Tum Jo Aaye",
    "/play Hasi Ban Gaye",
    "/play Jeene Laga Hoon",
    "/play Tum Hi Aana",
    "/play Duniyaa",
    "/play Galliyan",
    "/play Nazm Nazm",
    "/play Bol Do Na Zara",
    "/play Tera Ban Jaunga",
    "/play Soch Na Sake",
    "/play Tum Ho",
    "/play Tumhe Apna Banane Ka",
    "/play Aashiq Banaya Aapne",
    "/play Dil Diyan Gallan",
    "/play Zaalima",
    "/play Sab Tera",
    "/play Hawayein",
    "/play Piya O Re Piya",
    "/play Main Hoon Saath Tere",
    "/play Muskurane",
    "/play Saanson Ko",
    "/play Janam Janam",
    "/play Shayad",
    "/play Kaise Hua",
    "/play Thodi Jagah",
    "/play Tere Sang Yaara",
    "/play Khaab",
    "/play Aankhon Mein Teri",
    "/play Kaun Tujhe",
    "/play Samjhawan",
    "/play Paniyon Sa",
    "/play Hamari Adhuri Kahani",
    "/play Baarish",
    "/play Tera Fitoor",
    "/play Tum Mile",
    "/play Sun Le Zara",
    "/play Channa Mereya",
    "/play Kabira",
    "/play Laal Ishq",
    "/play Hawaayein",
    "/play Dhadak",
    "/play Tum Hi Ho",
    "/play Raabta",
    "/play Jeene Laga Hoon",
    "/play Pal",
    "/play Tum Hi Aana",
    "/play Mere Sohneya",
    "/play Shayad",
    "/play Ghungroo",
    "/play Ve Maahi",
    "/play Tujhe Kitna Chahne Lage",
    "/play Pehli Dafa",
    "/play Kaise Hua",
    "/play Dil Diyaan Gallan",
    "/play Khairiyat",
    "/play Hawayein",
    "/play Raanjhanaa",
    "/play Tum Mile",
    "/play Enna Sona",
    "/play Veer Zaara (Tere Liye)",
    "/play Tera Yaar Hoon Main",
    "/play Suno Na Sangemarmar",
    "/play Mile Ho Tum",
    "/play Dekhte Dekhte",
    "/play Hasi Ban Gaye",
    "/play Chale Aana",
    "/play Kalank",
    "/play Phir Le Aya Dil",
    "/play Tera Ban Jaunga",
    "/play Tum Jo Aaye",
    "/play Humdard",
    "/play Tu Hi Yaar Mera",
    "/play Kaise Hua",
    "/play Duniyaa",
    "/play Sun Saathiya",
    "/play Sanam Re",
    "/play Tum Mile",
    "/play Dil Meri Na Sune",
    "/play Tera Hone Laga Hoon",
    "/play Khuda Jaane",
    "/play Tujhe Kitna Chahein Aur",
    "/play Tum Jo Aaye Zindagi Mein",
    "/play Tum Se Hi",
    "/play Sun Le Zara",
    "/play Soch Na Sake",
    "/play Tum Ho",
    "/play Aashiq Banaya Aapne",
    "/play Tera Fitoor",
    "/play Piya O Re Piya"
]

item_songs = [
    "/play Sheila Ki Jawani",
    "/play Munni Badnaam Hui",
    "/play Chikni Chameli",
    "/play Fevicol Se",
    "/play Lungi Dance",
    "/play Anarkali Disco Chali",
    "/play Char Botal Vodka",
    "/play Babuji Zaara Dheere Chalo",
    "/play Koi Kahe Kehta Rahe",
    "/play Tere Mast Mast Do Nain",
    "/play Saana Kaay",
    "/play Aaja Nachle",
    "/play Chammak Challo",
    "/play Sadi Gali",
    "/play Chali Chali",
    "/play Main Tera Dushman",
    "/play Koi Kahe Kehta Rahe",
    "/play Raula Pai Gaya",
    "/play Aunty Ji",
    "/play Ooh La La",
    "/play Aa Re Pritam Pyaare",
    "/play Teri Khushboo",
    "/play Sona Sona",
    "/play Dil Mera Muft Ka",
    "/play Marjani",
    "/play Aa Toh Sahi",
    "/play Teri Khaani",
    "/play Pashmina",
    "/play Balam Pichkari",
    "/play Naino Mein Sapna",
    "/play Nasha",
    "/play Hawa Hawaai",
    "/play Ishq Shava",
    "/play Party All Night",
    "/play Dhating Naach",
    "/play Tujhko Jo Paaya",
    "/play Aaja Aaja",
    "/play Dhanno",
    "/play Mohini",
    "/play Aaja Nachle",
    "/play Tum Hi Ho Bandhu",
    "/play Jadoo Ki Jhappi",
    "/play Jeene Laga Hoon",
    "/play Gandi Baat",
    "/play Maari 2"
]

bhajan_songs = [
    "/play @Fancy_Waifu_Husbando_Bot collection.7506431563",
    "/play Hey Ram Hey Ram",
    "/play Achyutam Keshavam",
    "/play Raghupati Raghav Raja Ram",
    "/play Kabhi Ram Banke Kabhi Shyam Banke",
    "/play Tum Hi Ho Mata Pita Tum Hi Ho",
    "/play Bhajo Radhe Govinda",
    "/play Shree Krishna Govind Hare Murari",
    "/play Shiv Kailasho Ke Wasi",
    "/play Jag Mein Sundar Hain Do Naam",
    "/play Satnam Waheguru",
    "/play Hare Krishna Hare Rama",
    "/play Shankara Karunakara",
    "/play Jai Ambe Gauri",
    "/play Maiya Yashoda",
    "/play Mera Bhola Hai Bhandari",
    "/play Hanuman Chalisa",
    "/play Tumhi Ho Bandhu Sakha Tumhi Ho",
    "/play Mangal Bhavan Amangal Haari",
    "/play Ram Siya Ram",
    "/play Jai Lakshmi Mata",
    "/play Govind Bolo Hari Gopal Bolo",
    "/play Jagat Ke Rang Ka Rehna Nahi",
    "/play Vishnu Sahasranamam",
    "/play Shiv Tandav Stotram",
    "/play Ganesh Sharanam Sharanam",
    "/play Mere To Girdhar Gopal",
    "/play Radhe Radhe Barsane Wali Radhe",
    "/play Man Mera Mandir Shiv Meri Puja",
    "/play Radha Krishna Ki Jyoti Alokik",
    "/play Om Namah Shivaya",
    "/play Hari Om Sharan",
    "/play Devi Bhajans (Maa Durga)",
    "/play Jai Radha Madhav",
    "/play Jai Hanuman Gyan Gun Sagar",
    "/play Jai Jai Bhairav Nath",
    "/play Meera Ke Prabhu Giridhar Nagar",
    "/play Bolo Jai Jai Jai Hanuman",
    "/play Aarti Kunj Bihari Ki",
    "/play Om Jai Lakshmi Mata",
    "/play Ganga Stuti",
    "/play Shyam Teri Bansi",
    "/play O Palan Hare",
    "/play Mahalakshmi Ashtakam",
    "/play Gajanan Maharaj Ki Aarti",
    "/play Sukhkarta Dukhaharta",
    "/play Krishna Govind Govind Gopal Nandlal",
    "/play Radhe Radhe Japo",
    "/play Mantra Pushpam",
    "/play Hey Shambhu Baba Mere"
]

lofi_songs = [
    "/play Raatan Lambiyan (Lofi)",
    "/play Kabira (Lofi)",
    "/play Tum Hi Ho (Lofi)",
    "/play Khairiyat (Lofi)",
    "/play Agar Tum Saath Ho (Lofi)",
    "/play Phir Le Aya Dil (Lofi)",
    "/play Tum Mile (Lofi)",
    "/play Tera Ban Jaunga (Lofi)",
    "/play Shayad (Lofi)",
    "/play Channa Mereya (Lofi)",
    "/play Jeene Laga Hoon (Lofi)",
    "/play Raabta (Lofi)",
    "/play Tujhe Kitna Chahne Lage (Lofi)",
    "/play Dil Diyan Gallan (Lofi)",
    "/play Sun Saathiya (Lofi)",
    "/play Khamoshiyan (Lofi)",
    "/play Janam Janam (Lofi)",
    "/play Tum Jo Aaye (Lofi)",
    "/play Kaise Hua (Lofi)",
    "/play Samjhawan (Lofi)",
    "/play Laal Ishq (Lofi)",
    "/play Tum Se Hi (Lofi)",
    "/play Kal Ho Na Ho (Lofi)",
    "/play Aye Zindagi Gale Laga Le (Lofi)",
    "/play Muskurane (Lofi)",
    "/play Hasi Ban Gaye (Lofi)",
    "/play Tum Ho (Lofi)",
    "/play Main Phir Bhi Tumko Chahunga (Lofi)",
    "/play Hamari Adhuri Kahani (Lofi)",
    "/play Tum Hi Aana (Lofi)",
    "/play Pehli Nazar Mein (Lofi)",
    "/play Judaai (Lofi)",
    "/play Moh Moh Ke Dhaage (Lofi)",
    "/play Yeh Fitoor Mera (Lofi)",
    "/play Tera Hone Laga Hoon (Lofi)",
    "/play Kabira (Encore) (Lofi)",
    "/play Ranjha (Lofi)",
    "/play Humnava Mere (Lofi)",
    "/play Tum Mile (Lofi)",
    "/play Abhi Mujh Mein Kahin (Lofi)",
    "/play Ae Dil Hai Mushkil (Lofi)",
    "/play Soch Na Sake (Lofi)",
    "/play Khuda Jaane (Lofi)",
    "/play Baarish (Lofi)",
    "/play Hawayein (Lofi)",
    "/play Pal (Lofi)",
    "/play Tujh Mein Rab Dikhta Hai (Lofi)",
    "/play Sun Raha Hai Na Tu (Lofi)",
    "/play Phir Bhi Tumko Chaahunga (Lofi)"
]

emotional_songs = [
    "/play Tujhse Naraz Nahi Zindagi",
    "/play Agar Tum Saath Ho",
    "/play Channa Mereya",
    "/play Tum Hi Ho",
    "/play Kabira",
    "/play Phir Le Aya Dil",
    "/play Abhi Mujh Mein Kahin",
    "/play Khairiyat",
    "/play Hasi Ban Gaye",
    "/play Tera Yaar Hoon Main",
    "/play Phir Kabhi",
    "/play Tera Ban Jaunga",
    "/play Dil Diyan Gallan",
    "/play Tum Mile",
    "/play Tum Jo Aaye",
    "/play Kal Ho Naa Ho (Title Track)",
    "/play Zindagi Kaisi Hai Paheli",
    "/play Tu Hi Re",
    "/play Tum Hi Aana",
    "/play Raabta",
    "/play Sun Raha Hai Na Tu",
    "/play Yeh Dooriyan",
    "/play Duaa",
    "/play Shayad",
    "/play Kaise Hua",
    "/play Mere Haath Mein",
    "/play Humnava Mere",
    "/play Jeene Laga Hoon",
    "/play Judaai",
    "/play Zindagi Do Pal Ki",
    "/play Muskurane",
    "/play Khuda Jaane",
    "/play Tum Se Hi",
    "/play Raanjhanaa",
    "/play Pachtaoge",
    "/play Tum Mile",
    "/play Pehli Nazar Mein",
    "/play Saans",
    "/play Sun Saathiya",
    "/play Hamari Adhuri Kahani",
    "/play Main Tenu Samjhawan Ki",
    "/play Ae Dil Hai Mushkil (Title Track)",
    "/play Ae Watan",
    "/play Hamdard",
    "/play Kaun Tujhe",
    "/play Tujhe Kitna Chahne Lage",
    "/play Soch Na Sake",
    "/play Be Intehaan",
    "/play Aayat",
    "/play Dil Ke Paas",
    "/play Khamoshiyan",
    "/play Aye Zindagi Gale Laga Le",
    "/play Hasi Ban Gaye",
    "/play Janam Janam",
    "/play Tum Ho",
    "/play Tu Hi Yaar Mera",
    "/play Phir Bhi Tumko Chaahunga",
    "/play Baarish",
    "/play Ek Dil Hai",
    "/play Tujh Mein Rab Dikhta Hai",
    "/play Sun Le Zara",
    "/play Manzar Hai Yeh Naya",
    "/play Tum Mile",
    "/play Laal Ishq",
    "/play Maana Ke Hum Yaar Nahin",
    "/play Pal",
    "/play Dilbara",
    "/play Tum Na Aaye",
    "/play Tera Fitoor",
    "/play Tum Jo Aaye Zindagi Mein",
    "/play Ek Pyar Ka Nagma Hai",
    "/play Aaj Jaane Ki Zid Na Karo",
    "/play Jeene Laga Hoon",
    "/play Tum Bin",
    "/play Tu Hi Haqeeqat",
    "/play Saans",
    "/play Moh Moh Ke Dhaage",
    "/play Safarnama",
    "/play Yeh Fitoor Mera",
    "/play Dil Ibaadat",
    "/play Main Rahoon Ya Na Rahoon",
    "/play Pehli Dafa",
    "/play Judaai (Badlapur)",
    "/play Enna Sona",
    "/play Sun Le Zara",
    "/play Piya O Re Piya",
    "/play Jaane Nahi Denge",
    "/play Bulleya",
    "/play Tum Se Hi",
    "/play Kahin Toh Hogi Woh",
    "/play Tum Ho",
    "/play Bekhayali",
    "/play Main Phir Bhi Tumko Chahunga",
    "/play Tera Hone Laga Hoon",
    "/play Tum Hi Ho",
    "/play Ae Mere Humsafar",
    "/play Phir Le Aaya Dil",
    "/play Tum Mile",
    "/play Aaj Phir Tum Pe",
    "/play Tum Jo Aaye",
    "/play Kya Mujhe Pyaar Hai",
    "/play Raabta (Kehte Hain Khuda)"

]


# Global variables for tracking the current playback state
current_playlist = None
playing_index = 0
stop_playback = False

# Function to handle playlist commands
async def play_songs(event, song_list, start_index=0, end_index=None):
    global current_playlist, playing_index, stop_playback
    current_playlist = song_list
    playing_index = start_index
    stop_playback = False
    
    if end_index is None:
        end_index = len(song_list)
    
    songs_to_play = song_list[start_index:end_index]

    if not songs_to_play:
        await event.respond("No more songs to play.")
        return
    
    await event.respond(f"Starting Playlist from {start_index + 1} to {end_index}...")
    for song in songs_to_play:
        if stop_playback:
            break
        await bot.send_message(event.chat_id, song.strip())
        await asyncio.sleep(5)  # Adjust the delay as needed
        playing_index += 1

# Function to handle playlist display
async def show_playlist(event, song_list):
    playlist = "\n".join(song_list)
    await event.respond(f"Current Playlist:\n{playlist}")

# Handle playlist commands
@bot.on(events.NewMessage(outgoing=True, pattern=r'\.playrm(\d+)?(\d+-\d+)?'))
async def play_romantic(event):
    command = event.text
    count = None
    start_index = 0
    end_index = None
    if len(command) > 7:
        if '-' in command:
            start_index, end_index = map(int, command[7:].split('-'))
        else:
            count = int(command[7:])
    if end_index is None:
        end_index = start_index + count if count is not None else len(romantic_songs)
    await play_songs(event, romantic_songs, start_index, end_index)

@bot.on(events.NewMessage(outgoing=True, pattern=r'\.playbh(\d+)?(\d+-\d+)?'))
async def play_bhajan(event):
    command = event.text
    count = None
    start_index = 0
    end_index = None
    if len(command) > 7:
        if '-' in command:
            start_index, end_index = map(int, command[7:].split('-'))
        else:
            count = int(command[7:])
    if end_index is None:
        end_index = start_index + count if count is not None else len(bhajan_songs)
    await play_songs(event, bhajan_songs, start_index, end_index)

@bot.on(events.NewMessage(outgoing=True, pattern=r'\.playlofi(\d+)?(\d+-\d+)?'))
async def play_lofi(event):
    command = event.text
    count = None
    start_index = 0
    end_index = None
    if len(command) > 8:
        if '-' in command:
            start_index, end_index = map(int, command[8:].split('-'))
        else:
            count = int(command[8:])
    if end_index is None:
        end_index = start_index + count if count is not None else len(lofi_songs)
    await play_songs(event, lofi_songs, start_index, end_index)

@bot.on(events.NewMessage(outgoing=True, pattern=r'\.playitem(\d+)?(\d+-\d+)?'))
async def play_item(event):
    command = event.text
    count = None
    start_index = 0
    end_index = None
    if len(command) > 9:
        if '-' in command:
            start_index, end_index = map(int, command[9:].split('-'))
        else:
            count = int(command[9:])
    if end_index is None:
        end_index = start_index + count if count is not None else len(item_songs)
    await play_songs(event, item_songs, start_index, end_index)

@bot.on(events.NewMessage(outgoing=True, pattern=r'\.playem(\d+)?(\d+-\d+)?'))
async def play_emotional(event):
    command = event.text
    count = None
    start_index = 0
    end_index = None
    if len(command) > 8:
        if '-' in command:
            start_index, end_index = map(int, command[8:].split('-'))
        else:
            count = int(command[8:])
    if end_index is None:
        end_index = start_index + count if count is not None else len(emotional_songs)
    await play_songs(event, emotional_songs, start_index, end_index)

@bot.on(events.NewMessage(outgoing=True, pattern='.showlist'))
async def show_list(event):
    if current_playlist:
        await show_playlist(event, current_playlist)
    else:
        await event.respond("No playlist is currently active.")

@bot.on(events.NewMessage(outgoing=True, pattern='.stop'))
async def stop(event):
    global stop_playback
    stop_playback = True
    await event.respond("Stopping the playlist...")

bot.start()
bot.run_until_disconnected()
