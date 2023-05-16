from django.db.models import Count
from protocol.models import ProtocolData


def count_records():
    count = ProtocolData.objects.aggregate(total=Count('id'))
    return count['total']


def show_last_id_records():
    last_records = ProtocolData.objects.order_by('-id')[:3]
    last_ids = [record.id for record in reversed(last_records)]
    ids_string = str(last_ids)[1:-1]  # Удаление первого и последнего символа (квадратных скобок)
    return ids_string


def get_last_id():
    last_record = ProtocolData.objects.order_by('-id').first()
    if last_record:
        return last_record.id
    else:
        return None


def get_next_id():
    last_record = ProtocolData.objects.order_by('-id').first()
    if last_record:
        return last_record.id + 1
    else:
        return 1