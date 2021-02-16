import graphene
from graphene_django import DjangoObjectType
from task.models import task


class TaskTybe(DjangoObjectType):
    class Meta:
        model = task
        fields = ("id","cat_list","description","category","date")

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskTybe, id=graphene.Int())

    def resolve_all_tasks(root,info, id=None, *args, **kwargs):
        tasks = task.objects.all()
        if id is not None:
            tasks = task.objects.filter(id=id)
        return tasks

schema = graphene.Schema(query=Query)
