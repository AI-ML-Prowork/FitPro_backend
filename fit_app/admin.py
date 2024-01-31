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



from fit_app.models import Add_reward
class Add_rewardAdmin(admin.ModelAdmin):
    list_display = ('username', 
                    'steps_count', 
                    'calories_burn', 
                    'rewards', 
                    'last_login', 
                    'registration_date_time', 
                    'age'
                    )
    

admin.site.register(Add_reward, Add_rewardAdmin)    


from fit_app.models import Add_Order
class Add_OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 
                    'item_name', 
                    'amount', 
                    'user', 
                    'steps_count', 
                    'calories_burn', 
                    'rewards', 
                    'date_time'
                    )
    

admin.site.register(Add_Order, Add_OrderAdmin)  
