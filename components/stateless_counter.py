from django_components import component


@component.register("stateless_counter")
class StatelessCounterComponent(component.Component):
    def get_context_data(self, id, **kwargs):
        return {"count": 0, "id": id}

    def post(self, request, method, id, *args, **kwargs):
        if method == "inc":
            count = int(request.POST.get("count", 0)) + 1
        elif method == "dec":
            count = int(request.POST.get("count", 0)) - 1
        context = {
            "count": count,
            "id": id,
        }
        slots = {}
        return self.render_to_response(context, slots)

    template = """
        <div id="stateless-counter-component-{{ id }}" 
             hx-target="#stateless-counter-component-{{ id }}" 
             hx-vals='{ "count": {{ count}} }'>
            <div>Count: {{ count }}</div>
            <button type="button" hx-post="{% url 'stateless_counter' method='dec' id=id %}"> -1 </button>
            <button type="button" hx-post="{% url 'stateless_counter' method='inc' id=id %}"> +1 </button>
        </div>
    """
