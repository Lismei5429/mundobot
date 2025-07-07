from telegram.ext import Updater, CommandHandler

# Función cuando el usuario inicia el bot con /start
def start(update, context):
    update.message.reply_text("¡Hola! Bienvenido al bot de minería 💎\n\nUsa /menu para ver las opciones.")

# Comando adicional de ejemplo: /menu
def menu(update, context):
    update.message.reply_text("📋 Menú Principal:\n\n🔹 /start - Iniciar bot\n🔹 /menu - Mostrar menú\n🔹 Próximamente más funciones...")

# TOKEN DEL BOT
TOKEN = "7771234555:AAHiQY8MtKVxu30VuQdxbNwmyna6E1UnET8"

# Iniciando el bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Asignar comandos
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("menu", menu))

# Arrancar el bot
updater.start_polling()
updater.idle()
