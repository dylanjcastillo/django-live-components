from django_components import component
from app.models import Counter


@component.register("counter")
class CounterComponent(component.Component):
    model = Counter

    def get_context_data(self, id, **kwargs):
        counter, _ = self.model.objects.get_or_create(id=id)
        return {"count": counter.count, "id": id}

    def post(self, request, method, id, *args, **kwargs):
        counter, _ = self.model.objects.get_or_create(id=id)

        if method == "inc":
            counter.count += 1
            counter.save()
        elif method == "dec":
            counter.count -= 1
            counter.save()

        context = {
            "count": counter.count,
            "id": id,
        }
        slots = {}
        return self.render_to_response(context, slots)

    template = """
        <div id="counter-component-{{ id }}" hx-target="#counter-component-{{ id }}">
            <div>Count: {{ count }}</div>
            <button type="button" hx-post="{% url 'counter' method='dec' id=id %}"> -1 </button>
            <button type="button" hx-post="{% url 'counter' method='inc' id=id %}"> +1 </button>
        </div>
    """
