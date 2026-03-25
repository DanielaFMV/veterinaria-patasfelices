 # 🐾 Veterinaria PatasFelices                                                                                         
                                                                                                                        
  Sistema de gestión CRUD para la clínica veterinaria ficticia **PatasFelices**, desarrollado con Django.               
                  
  ## Descripción                                                                                                        
                  
  Aplicación web que permite gestionar dueños, mascotas y consultas médicas mediante operaciones CRUD completas         
  accesibles desde el navegador.
                                                                                                                        
  ## Tecnologías  

  - Python 3.14
  - Django 6.0
  - SQLite (desarrollo)
  - PostgreSQL / Supabase (producción)
                                                                                                                        
  ## Funcionalidades
                                                                                                                        
  - Gestión de **Dueños**: crear, listar, ver detalle, editar y eliminar                                                
  - Gestión de **Mascotas**: crear, listar, ver detalle, editar y eliminar
  - Historial de **Consultas Médicas** por mascota                                                                      
  - Panel de administración personalizado
  - Precios en formato CLP ($10.000)                                                                                    
  - Fechas en formato DD/MM/AA                                                                                          
                                                                                                                        
  ## Instalación                                                                                                        
                  
  ```bash
  # Clonar el repositorio
  git clone https://github.com/DanielaFMV/veterinaria-patasfelices.git                                                  
  cd veterinaria-patasfelices
                                                                                                                        
  # Crear y activar entorno virtual
  python3 -m venv veterinaria_env                                                                                       
  source veterinaria_env/bin/activate
                                                                                                                        
  # Instalar dependencias
  pip install django python-dotenv dj-database-url psycopg2-binary                                                      
                  
  # Crear archivo .env basado en .env.example                                                                           
  cp .env.example .env
                                                                                                                        
  # Aplicar migraciones
  python manage.py migrate

  # Crear superusuario
  python manage.py createsuperuser
                                                                                                                        
  # Ejecutar servidor
  python manage.py runserver                                                                                            
                  
  Estructura del proyecto

  veterinaria_patasfelices/
  ├── fichas/              # App principal
  │   ├── models.py        # Modelos: Dueno, Mascota, ConsultaMedica                                                    
  │   ├── views.py         # Vistas CRUD con Class-Based Views                                                          
  │   ├── urls.py          # Rutas de la app                                                                            
  │   └── admin.py         # Panel de administración                                                                    
  ├── templates/fichas/    # Templates HTML
  ├── veterinaria_patasfelices/                                                                                         
  │   └── settings/        # Configuración separada por entorno                                                         
  │       ├── base.py                                                                                                   
  │       ├── development.py                                                                                            
  │       └── production.py                                                                                             
  ├── .env.example
  └── manage.py   