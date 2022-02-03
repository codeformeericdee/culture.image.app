from django.contrib import admin
from database_models.models import Region, RegionReferencePoint
from database_models.models import GlobalSymbol, GlobalSymbolReferencePoint
from database_models.models import UserSymbol, UserSymbolType, UserSymbolReferencePoint

#Countries:
class InlineRegionReferencePoint(admin.StackedInline):
    model = RegionReferencePoint
    extra = 1

class AdministrateRegion(admin.ModelAdmin):
    inlines = [InlineRegionReferencePoint]

admin.site.register(Region, AdministrateRegion)
admin.site.register(RegionReferencePoint)

# Global symbols:
class InlineGlobalSymbolReferencePoint(admin.StackedInline):
    model = GlobalSymbolReferencePoint
    extra = 1

class AdministrateGlobalSymbol(admin.ModelAdmin):
    inlines = [InlineGlobalSymbolReferencePoint]
    exclude = ['region_int_id']

admin.site.register(GlobalSymbol, AdministrateGlobalSymbol)
admin.site.register(GlobalSymbolReferencePoint)

# User symbols:
class InlineUserSymbolReferencePoint(admin.StackedInline):
    model = UserSymbolReferencePoint
    extra = 1
    fk_name = 'symbol_image_id' # AKA Use the FK that makes sense to the backend

class AdministrateUserSymbol(admin.ModelAdmin):
    inlines = [InlineUserSymbolReferencePoint]

admin.site.register(UserSymbol, AdministrateUserSymbol)

admin.site.register(UserSymbolType)
admin.site.register(UserSymbolReferencePoint)