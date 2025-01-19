from prefect import flow
from task.task_extract_linkedin import task_extract_linkedin
from task.task_load_linkedin import task_load_linkedin


@flow(name="ETL-LINKDIN")
def main_flow():
    print("Inicio del flujo...")
    print("Inicio de extraccion...")
    ofertas=task_extract_linkedin()
    print("Inicio de carga...")
    task_load_linkedin(ofertas)
    

        
if __name__ == "__main__":
    main_flow()