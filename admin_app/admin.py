from django.contrib import admin

from admin_app.models import Add_Product
class Add_ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 
                    'description', 
                    'price', 
                    'quantity', 
                    'additionalField1', 
                    'additionalField2', 
                    'additionalField3', 
                    'additionalField4', 
                    'additionalField5'
                    )

admin.site.register(Add_Product, Add_ProductAdmin)


# from admin_app.models import UserProfile
# class UserProfileInline(admin.ModelAdmin):
#     list_display = ('user_name', 
#                     'age', 
#                     'height', 
#                     'weight', 
#                     'any_disease', 
#                     'allergies'
#                     )


# admin.site.register(UserProfile, UserProfileInline)


from admin_app.models import Ordered_Product
class Ordered_ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 
                    'quantity', 
                    'size', 
                    'price', 
                    'date'
                    )

admin.site.register(Ordered_Product, Ordered_ProductAdmin)



# from admin_app.models import Wallet
# class WalletAdmin(admin.ModelAdmin):
#     list_display = ('amount', 
#                     'payment_mode', 
#                     'date'
#                     )
    
# admin.site.register(Wallet, WalletAdmin)