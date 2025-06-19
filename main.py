crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}
user_query = input("What would you like to know about crypto today?\n").lower()

if "sustainable" in user_query:
    best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"Try {best}! 🌱 It's eco-friendly and has long-term potential.")
elif "profitable" in user_query or "buy" in user_query:
    for name, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            print(f"{name} looks profitable right now! 📈")
            break
else:
    print("Hmm, I’m not sure. Ask me about sustainability or profitability.")
