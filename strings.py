from pyrogram.types import InlineKeyboardButton
from creds import cred

welcome = "`Give me the subtitle file you want to translate..`"
about = (
    "`Bot`            : [subtransbot](t.me/subtransbot)\n`Creator :` [agentnova](t.me/agentnova)\n`Language:` ["
    "Python3](https://python.org)\n`Library :` [Pyrogram](https://docs.pyrogram.org/) \n`Server  :` [Heroku]("
    "https://herokuapp.com/) "
)
help_text = (
    "**Steps to follow**\n\n`This is a subtitle translator bot`\n**1.** `Send me the subtitle file inorder to "
    "translate.`\n**2.** `Select the destination language(dont press multiple buttons).`\n**3.** `Wait some time "
    "to complete the translation.`\n\n**Keep in mind**\n\n**1.** `You can only translate one subtitle at a "
    "time`\n**2.** `Dont forward bulk files together , You will be banned` "
)
eta_text = (
    "**File name :** `{}`\n**Done** `{}` **of** `{}`\n**Percentage:** {}%\n**Speed:** {} lines/sec\n**ETA:** {}\n[{"
    "}{}] "
)
caption = f"Translated by {cred.BOT_NAME}"
empty = "`You need to send a subtitle(srt) file inorder to translate it`"
mmtypes = [
    "text/plain",
    "application/x-subrip",
    "application/octet-stream",
    "application/binary",
]
err1 = "**__One subtitle is processing wait sometime__**"
err2 = "**__This is not a subtitle(srt) file__**"
err3 = "**Todays limit exceeded**"
err4 = "**Unsupported characters in file**"
err5 = "**Some errors happened Try again..**"

langs = [
    [
        InlineKeyboardButton("മലയാളം", callback_data="Malayalam"),
        InlineKeyboardButton("தமிழ்", callback_data="Tamil"),
        InlineKeyboardButton("हिन्दी", callback_data="Hindi"),
    ],
    [
        InlineKeyboardButton("ಕನ್ನಡ", callback_data="Kannada"),
        InlineKeyboardButton("తెలుగు", callback_data="Telugu"),
        InlineKeyboardButton("मराठी", callback_data="Marathi"),
    ],
    [
        InlineKeyboardButton("ગુજરાતી", callback_data="Gujarati"),
        InlineKeyboardButton("ଓଡ଼ିଆ", callback_data="Odia"),
        InlineKeyboardButton("বাংলা", callback_data="bn"),
    ],
    [
        InlineKeyboardButton("ਪੰਜਾਬੀ", callback_data="Punjabi"),
        InlineKeyboardButton("فارسی", callback_data="Persian"),
        InlineKeyboardButton("English", callback_data="English"),
    ],
    [
        InlineKeyboardButton("español", callback_data="Spanish"),
        InlineKeyboardButton("français", callback_data="French"),
        InlineKeyboardButton("русский", callback_data="Russian"),
    ],
    [
        InlineKeyboardButton("עִברִית", callback_data="hebrew"),
        InlineKeyboardButton("العربية", callback_data="arabic"),
        InlineKeyboardButton("සිංහල",callback_data="sinhala"),
    ],
]
