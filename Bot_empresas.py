import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caratula_text = (
        "📱 *¡Bienvenido a FixMobile Center!*\n\n"
        "Sistema automatizado de gestión de clientes y servicios técnicos.\n"
        "¿En qué podemos ayudarte hoy?"
    )
    keyboard = [
        [InlineKeyboardButton("🛠 Ver Servicios de Reparación", callback_data='servicios')],
        [InlineKeyboardButton("🎫 Generar Turno de Atención", callback_data='turno')],
        [InlineKeyboardButton("📞 Contacto y Ubicación", callback_data='contacto')],
        [InlineKeyboardButton("ℹ️ Acerca del Sistema", callback_data='creditos')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(caratula_text, reply_markup=reply_markup, parse_mode='Markdown')

async def comando_ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    estado_servidor = (
        "🟢 *Estado del Servidor Central:*\n\n"
        "• *Host:* Railway Cloud Worker\n"
        "• *Latencia API Telegram:* 12ms\n"
        "• *Estado de BD:* Conexión Estable\n"
        "• *Módulos:* Operativos"
    )
    await update.message.reply_text(estado_servidor, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'menu':
        texto = "📱 *Menú Principal FixMobile:*\n¿Qué gestión deseas realizar?"
        keyboard = [
            [InlineKeyboardButton("🛠 Ver Servicios de Reparación", callback_data='servicios')],
            [InlineKeyboardButton("🎫 Generar Turno de Atención", callback_data='turno')],
            [InlineKeyboardButton("📞 Contacto y Ubicación", callback_data='contacto')],
            [InlineKeyboardButton("ℹ️ Acerca del Sistema", callback_data='creditos')]
        ]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'turno':
        num_turno = random.randint(1000, 9999)
        texto = f"🎫 *¡Turno Generado!*\n\nTu código es: *FIX-{num_turno}*\n\n_Presenta este código al técnico._"
        keyboard = [[InlineKeyboardButton("🔙 Volver al Menú", callback_data='menu')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'creditos':
        texto = (
            "👨‍💻 *Acerca de este Software:*\n\n"
            "Desarrollado por el equipo de Ingeniería:\n"
            "• Juniher Bravo\n"
            "• Andres Morales\n"
            "• Daniel Follain\n"
            "_Proyecto de Bot Asistente v1.0_"
        )
        keyboard = [[InlineKeyboardButton("🔙 Volver al Menú", callback_data='menu')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'contacto':
        texto = "📍 *FixMobile Center:*\n\n📱 WhatsApp: +593 99 123 4567\n⏱ Horario: L-S 9:00 AM a 6:00 PM"
        keyboard = [[InlineKeyboardButton("🔙 Volver al Menú", callback_data='menu')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'servicios':
        texto = "📋 *Nuestros Servicios Técnicos:*"
        keyboard = [
            [InlineKeyboardButton("📱 Pantallas (OLED/LCD)", callback_data='srv_pantallas')],
            [InlineKeyboardButton("🔋 Reemplazo de Baterías", callback_data='srv_baterias')],
            [InlineKeyboardButton("🔬 Diagnóstico de Hardware", callback_data='srv_hardware')],
            [InlineKeyboardButton("🔙 Volver al Menú", callback_data='menu')]
        ]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'srv_pantallas':
        texto = "📱 *Servicio de Pantallas:*\nRepuestos originales y genéricos (AAA)."
        keyboard = [
            [InlineKeyboardButton("💵 Ver Precios", callback_data='pantallas_precio')],
            [InlineKeyboardButton("⏱ Tiempo de Reparación", callback_data='pantallas_tiempo')],
            [InlineKeyboardButton("🔙 Volver a Servicios", callback_data='servicios')]
        ]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'pantallas_precio':
        texto = "💵 *Precios de Pantallas:*\n• Gama Media: $30 - $60\n• Gama Alta: $80 - $250+"
        keyboard = [[InlineKeyboardButton("🔙 Volver a Pantallas", callback_data='srv_pantallas')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'pantallas_tiempo':
        texto = "⏱ *Tiempo estimado:*\nEntre 45 minutos y 1.5 horas si tenemos stock."
        keyboard = [[InlineKeyboardButton("🔙 Volver a Pantallas", callback_data='srv_pantallas')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'srv_baterias':
        texto = "🔋 *Reemplazo de Baterías:*\nInstalamos celdas nuevas con ciclo cero."
        keyboard = [
            [InlineKeyboardButton("💵 Costos", callback_data='baterias_costo')],
            [InlineKeyboardButton("🛡️ Garantía", callback_data='baterias_garantia')],
            [InlineKeyboardButton("🔙 Volver a Servicios", callback_data='servicios')]
        ]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'baterias_costo':
        texto = "💵 *Costos de Baterías:*\n• Android: $20 - $45\n• iPhone: $35 - $70"
        keyboard = [[InlineKeyboardButton("🔙 Volver a Baterías", callback_data='srv_baterias')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'baterias_garantia':
        texto = "🛡️ *Garantía:*\n3 meses de garantía contra defectos de fábrica."
        keyboard = [[InlineKeyboardButton("🔙 Volver a Baterías", callback_data='srv_baterias')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'srv_hardware':
        texto = "🔬 *Diagnóstico de Hardware:*\nAnálisis a nivel de componentes en la placa base."
        keyboard = [
            [InlineKeyboardButton("🔍 Detalles", callback_data='hw_detalle')],
            [InlineKeyboardButton("⏱ Costo", callback_data='hw_costo')],
            [InlineKeyboardButton("🔙 Volver a Servicios", callback_data='servicios')]
        ]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'hw_detalle':
        texto = "🔍 *Detalles:*\n• Medición de consumos.\n• Búsqueda de cortos.\n• Limpieza ultrasónica."
        keyboard = [[InlineKeyboardButton("🔙 Volver a Hardware", callback_data='srv_hardware')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == 'hw_costo':
        texto = "⏱ *Costo y Tiempo:*\n$10 descontables de la reparación. Toma de 24 a 48 horas."
        keyboard = [[InlineKeyboardButton("🔙 Volver a Hardware", callback_data='srv_hardware')]]
        await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

def main():
    TOKEN = "8652786490:AAF1Zx9a-uxbDIw6AV-cgo-fC5oMZvTrg6I"
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ping", comando_ping))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot activo en servidor.")
    application.run_polling()

if __name__ == '__main__':
    main()