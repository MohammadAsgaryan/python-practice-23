try:
    user_input = input("یک عدد وارد کنید: ")

    # تلاش برای تبدیل ورودی به عدد
    number = float(user_input)

    if number == 0:
        print("❌ تقسیم بر صفر امکان‌پذیر نیست.")
    else:
        result = 100 / number
        print(f"✅ نتیجه: 100 ÷ {number} = {result}")
except ValueError:
    print("⚠️ لطفاً فقط عدد وارد کنید، متن مجاز نیست.")
except Exception as e:
    print(f"🚨 خطای غیرمنتظره رخ داد: {e}")
