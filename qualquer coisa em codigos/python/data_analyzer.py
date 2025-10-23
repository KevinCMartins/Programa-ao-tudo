import json
import csv
import random
import statistics
import datetime
from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class SalesRecord:
    date: str
    product: str
    category: str
    quantity: int
    price: float
    customer_id: str
    region: str

    @property
    def total_value(self) -> float:
        return self.quantity * self.price
    
    @property
    def month(self) -> str:
        return self.date[:7] 
    
class DataGenerator:

    PRODUCTS = [
        'Laptop PRO', 'Smartphone X', 'Tablet Air', 'Headphones Elite',
         'Smart Watch', 'Gaming Console', 'Wireless Speaker', 'Camera Pro',
           'Monitor 4K', 'Keyboard Mechanical', 'Mouse Wireless', 'Printer Laser'
    ]

    CATEGORIES = ['Electronics', 'Computers', 'Audio', 'Gaming', 'Accessories']
    REGIONS = ['North', 'South', 'East', 'West', 'Central']

    @staticmethod
    def gererate_sales_data(num_records: int = 1000) -> List[SalesRecord]:
        records = []
        start_date = datetime.date(2023, 1, 1)

        for i in range(num_records):
            random_days = random.randint(0, 364)
            record_date = start_date + datetime.timedelta(days=random_days)

            product = random.choice(DataGenerator.PRODUCTS)
            category = random.choice(DataGenerator.CATEGORIES)
            quantity = random.randint(1, 10)
            price = round(random.uniform(50, 2000), 2)
            custumer_id = f'CUST_{random.randint(1000, 9999)}'
            region = random.choice(DataGenerator.REGIONS)

            record = SalesRecord(
                date=record_date.strftime('%Y-%m-%d'),
                product=product,
                category=category,
                quantity=quantity,
                price=price,
                customer_id=custumer_id,
                region=region
            )
            record.append(record)

        return records

class DataAnalyzer:

    def __init__(self, data: List[SalesRecord]):
        self.data = data
        self.analysis_results = {}

    def basic_statistics(self) -> Dict[str, Any]:
        total_records = len(self.data)
        total_revenue = sum(record.total_value for record in self.data)
        total_quantity = sum(record.quantity for record in self.data)

        prices = [record.price for record in self.data]
        quantities = [record.quantity for record in self.data]

        stats = {
            'total_records': total_records,
            'total_revenue': round(total_revenue, 2),
            'total_quantity': total_quantity,
            'average_price': round(statistics.mean(prices), 2),
            'median_price': round(statistics.median(prices), 2),
            'price_std_dev': round(statistics.stdev(prices), 2),
            'average_quantity': round(statistics.mean(quantities), 2),
            'unique_products': len(set(record.products for record in self.data)),
            'unique_costumers': len(set(record.costumer_id for record in self.data))
        }

        self.analysis_results['basic_stats'] = stats
        return stats
    def analyze_by_category(self) -> Dict[str, Dict[str, float]]:
        category_data = defaultdict(lambda: {'revenue': 0, 'quantity': 0, 'count': 0})

        for record in self.data:
            category_data[record.category]['revenue'] += record.total_value
            category_data[record.category]['quantity'] += record.quantity
            category_data[record.category]['count'] += 1

        result = {}
        for region, data in region_data.items():
            result[region] = {
                'total_revenue': round(data['revenue'], 2),
                'total_quantity': data['quantity'],
                'total_orders': data['count'],
                'avg_order_value': round(data['revenue'] / data['count'], 2),
                'avg_quantity_per_order': round(data['quantity'] / data['count'], 2)
            }

        self.analysis_results['category_analysis'] = result
        return result
    
    def analyze_by_region(self) -> Dict[str, Dict[str, float]]:
        region_data = defaultdict(lambda: {'revenue': 0, 'quantity': 0, 'count': 0})

        for record in self.data:
            region_data[record.region]['revenue'] += record.total_value
            region_data[record.region]['quantity'] += record.quantity
            region_data[record.region]['count'] += 1

        result = {}
        for region, data in region.items():
            result[region] = {
                'total_revenue': round(data['revenue'], 2),
                'total_quantity': data['quantity'],
                'total_orders': data['count'],
                'avg_order_value': round(data['revenue'] / data['count'], 2)
            }

        self.analysis_results['region_analysis'] = result
        return result
    
    def monthly_trends(self) -> Dict[str, Dict[str, float]]:
        """Analyze monthly sales trends"""
        monthly_data = defaultdict(lambda: {"revenue": 0, "quantity": 0, "count": 0})
        
        for record in self.data:
            month = record.month
            monthly_data[month]["revenue"] += record.total_value
            monthly_data[month]["quantity"] += record.quantity
            monthly_data[month]["count"] += 1
        
        result = {}
        for month, data in monthly_data.items():
            result[month] = {
                "total_revenue": round(data["revenue"], 2),
                "total_quantity": data["quantity"],
                "total_orders": data["count"],
                "avg_order_value": round(data["revenue"] / data["count"], 2)
            }
        
        self.analysis_results["monthly_trends"] = result
        return result
    
    def top_products(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Find top-selling products"""
        product_data = defaultdict(lambda: {"revenue": 0, "quantity": 0, "count": 0})
        
        for record in self.data:
            product_data[record.product]["revenue"] += record.total_value
            product_data[record.product]["quantity"] += record.quantity
            product_data[record.product]["count"] += 1

        sorted_products = sorted(
            product_data.items(),
            key=lambda x: x[1]['revenue'],
            reverse=True
        )

        result = []
        for product, data in sorted_products[:limit]:
            result.append({
                'product': product,
                'total_revenue': round(data['revenue'], 2),
                'total_quantity': data['quantity'],
                'total_orders': data['count'],
                'avg_price': round(data['revenue'] / data['quantity'], 2)
            })

        self.analysis_results['top_products'] = result
        return result
    
    def customer_analysis(self) -> Dict[str, Any]:
        customer_data = defaultdict(lambda: {'revenue': 0, 'orders': 0, 'quantity': 0})

        for record in self.data:
            customer_data[record.customer_id]["revenue"] += record.total_value
            customer_data[record.customer_id]["orders"] += 1
            customer_data[record.customer_id]["quantity"] += record.quantity

        revenues = [data['revenue' for data in customer_data.values()]]
        orders = [data['orders' for data in customer_data.values()]]

        top_customers = sorted(
            customer_data.items(),
            key=lambda x: x[1]['revenue'],
            reverse=True
        )[:10]

        result = {
            'total_customers': len(customer_data),
            'avg_revenue_per_customer': round(statistics.mean(revenues), 2),
            'median_revenue_per_customers': round(statistics.median(revenues), 2),
            'avg_orders_ per_customer': round(statistics.mean(orders), 2),
            'top_customers': [
                {
                    'customer_id': customer,
                    'total_revenue': round(data['revenue'], 2),
                    'total_orders': data['orders'],
                    'avg_order_value': round(data['revenue'] / data['quantity'], 2)
                }
                for customer, data in top_customers
            ]
        }

        self.analysis_results['customer_analysis'] = result
        return result

class DataVisualizer:

    def __init__(self, analyzer: DataAnalyzer):
        self.analyzer = analyzer
        plt.style.use('default')

    def plot_cataegory_revenue(self):
        if 'category_analysis' not in self.analyzer.analysis_results:
            self.analyzer.analyze_by_category()

        data = self.analyzer.analysis_results['category_analysis']
        categories = list(datsa.keys())
        revenues = [data[cat]['total_revenue'] for cat in categories]

        plt.figure(fig.siz)