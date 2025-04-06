import requests
from config import TELEGRAM_BOT_TOKEN, CHAT_ID  # Importação corrigida

def enviar_notificacao(time_casa, time_fora, competicao, tempo):
    """Envia alerta para seu Telegram"""
    mensagem = (
        f"⚽ ALERTA 0x0 ⚽\n\n"
        f"🏆 {competicao}\n"
        f"⏱️ {tempo}\n\n"
        f"{time_casa} 0 × 0 {time_fora}"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, params=params, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"⚠️ Erro no Telegram: {str(e)}")
        if hasattr(e, 'response'):
            print(f"Resposta do Telegram: {e.response.text}")