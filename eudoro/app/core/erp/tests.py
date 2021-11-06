import random
from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import Coalesce

from core.erp.models import Sale, SaleDetail

for m in range(0, 6):
    pedids = random.randint(18, 29)
    for d in range(1, pedids):
        vent = Sale()
        vent.cli_id = random.randint(1, 3)
        vent.date_joined = datetime(2020, m + 1, d)
        vent.save()

        food = random.randint(1, 10)

        for i in range(0, food):
            det = SaleDetail()
            det.sale_id = vent.id
            det.product_id = random.randint(1, 23)
            det.price = det.product.pvp
            det.quantity = random.randint(1, 4)
            det.subtotal = float(det.price) * det.quantity
            det.save()

        vent.subtotal = vent.saledetail_set.all().aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
        vent.igv = float(vent.subtotal) * 0.12
        vent.total = float(vent.subtotal) + float(vent.igv)
        vent.save()
print('Terminado')
