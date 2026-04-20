from flask import Blueprint, render_template, request, request
from models.venta import Venta  
from models.vendedor import Vendedor
from models.regla import Regla
from datetime import datetime


venta_bp = Blueprint('ventas', __name__)

@venta_bp.route('/', methods=['GET', 'POST'])
def resumen_comisiones():
    comisiones = []
    fecha_inicio = request.form.get('fecha_inicio')
    fecha_fin = request.form.get('fecha_fin')
    
    vendedores = Vendedor.query.all()
    reglas = Regla.query.order_by(Regla.monto_minimo.desc()).all()
    for vendedor in vendedores:
        if fecha_inicio and fecha_fin:
            fi = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            ff = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
            ventas = Venta.query.filter(
                Venta.vendedor_id == vendedor.id,
                Venta.fecha_venta >= fi,
                Venta.fecha_venta <= ff
            ).all()
        else:
            ventas = Venta.query.filter_by(vendedor_id=vendedor.id).all()
            
        total_ventas = sum(v.cuota_monto for v in ventas)
        if total_ventas == 0:
            continue

        porcentaje = 0
        for regla in reglas:
            if total_ventas >= regla.monto_minimo:
                porcentaje = regla.porcentaje_comision
                break
        comision = total_ventas * (porcentaje / 100)

        comisiones.append({
            'vendedor': vendedor.nombre,
            'total_ventas': total_ventas,
            'porcentaje': porcentaje,
            'comision': comision
    })
    return render_template('index.html', comisiones=comisiones, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)