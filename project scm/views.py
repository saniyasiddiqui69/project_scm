from django.shortcuts import render

def dashboard(request):
    dashboard_data = {
        'total_products': 1280,
        'orders_placed': 320,
        'total_revenue': 45000,
        'pending_deliveries': 18,
    }

    context = {
        'dashboard_data': dashboard_data,
    }
    return render(request, 'dashboard.html', context)
