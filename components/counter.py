from django_components import component
from app.models import Counter


@component.register("counter")
class CounterComponent(component.Component):
    model = Counter

    def get_context_data(self, id, **kwargs):
        counter, _ = self.model.objects.get_or_create(id=id)
        return {"count": counter.count}

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
        }
        slots = {}
        print("POST", context, slots)
        
        return self.render_to_response(context, slots)

    template = """
        <div id="counter-component" hx-target="#counter-component">
            <span>Count: {{ count }}</span>
            <button type="button" hx-post="{% url 'counter' method='inc' id=1 %}">Increment</button>
            <button type="button" hx-post="{% url 'counter' method='dec' id=1 %}">Decrement</button>
        </div>
    """

    css = """
        .calendar-component { width: 200px; background: pink; }
        .calendar-component span { font-weight: bold; }
    """

    js = """
    """
