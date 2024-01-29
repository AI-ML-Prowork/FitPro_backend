from django.contrib import admin


from fit_app.models import UserProfile
class UserProfileInline(admin.ModelAdmin):
    list_display = ('user_name', 
                    'age', 
                    'height', 
                    'weight', 
                    'any_disease', 
                    'allergies'
                    )


admin.site.register(UserProfile, UserProfileInline)



from fit_app.models import Wallet
class WalletAdmin(admin.ModelAdmin):
    list_display = ('amount', 
                    'payment_mode', 
                    'date'
                    )
    
admin.site.register(Wallet, WalletAdmin)
