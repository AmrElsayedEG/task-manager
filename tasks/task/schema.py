import graphene
from graphene_django import DjangoObjectType
from task.models import task

#Types

class TaskTybe(DjangoObjectType):
    class Meta:
        model = task
        fields = ("id","description","category","date")

#Query
        
class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskTybe, id=graphene.Int())

    def resolve_all_tasks(root,info, id=None, *args, **kwargs):
        tasks = task.objects.all()
        if id is not None:
            tasks = task.objects.filter(id=id)
        return tasks


#Mutation

class AddTaskMutation(graphene.Mutation):
    tasks = graphene.Field(TaskTybe)
    
    class Arguments:
        description = graphene.String(required=True)
        category = graphene.String(required=True)
        date = graphene.Date(required=True)
    
    
    @classmethod
    def mutate(cls, root, info, description, category, date, *args, **kwargs):
        tasks = task(description=description,category=category,date=date)
        tasks.save()
        return AddTaskMutation(tasks=tasks)
        

class UpdateTaskMutation(graphene.Mutation):
    tasks = graphene.Field(TaskTybe)
    
    class Arguments:
        id = graphene.ID()
        description = graphene.String(required=True)
        category = graphene.String(required=True)
        date = graphene.Date(required=True)

    @classmethod
    def mutate(cls, root, info, id, description, category, date, *args, **kwargs):
        tasks = task.objects.get(id=id)
        tasks.description = description
        tasks.category = category
        tasks.date = date
        tasks.save()
        return UpdateTaskMutation(tasks=tasks)

class DeleteTaskMutation(graphene.Mutation):
    tasks = graphene.Field(TaskTybe)
    
    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, id, *args, **kwargs):
        tasks = task.objects.get(id=id)
        tasks.delete()
        return

class Mutation(graphene.ObjectType):
    add_task = AddTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()
    delete_task = DeleteTaskMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
