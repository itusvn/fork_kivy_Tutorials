import mysql.connector

host = "localhost"
user = "root"
passwd = ""
db = "hospital"

def connection():
    return mysql.connector.connect(host=host, user=user, password=passwd, database=db)

def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(255),
            role VARCHAR(50),
            password TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS staff (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            name VARCHAR(255),
            position VARCHAR(100),
            department VARCHAR(100),
            phone VARCHAR(255),
            email VARCHAR(255),
            address TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS patients (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            name VARCHAR(255),
            dob DATE,
            gender VARCHAR(10),
            phone VARCHAR(255),
            email VARCHAR(255),
            address TEXT,
            blood_type VARCHAR(10),
            medical_history TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS appointments (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            patient_id INTEGER REFERENCES patients(id),
            staff_id INTEGER REFERENCES staff(id),
            date DATE,
            time TIME,
            reason TEXT,
            status VARCHAR(50)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS rooms (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            room_number VARCHAR(10),
            type VARCHAR(50),
            capacity INTEGER,
            status VARCHAR(50),
            notes TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS beds (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            room_id INTEGER REFERENCES rooms(id),
            bed_number VARCHAR(10),
            status VARCHAR(50),
            patient_id INTEGER REFERENCES patients(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS sales (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            patient_id INTEGER REFERENCES patients(id),
            date DATE,
            item TEXT,
            amount DECIMAL(12, 2),
            method VARCHAR(50),
            notes TEXT
        );
        """,
        """CREATE TABLE IF NOT EXISTS consultations(
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            patient_id INTEGER REFERENCES patients(id),
            staff_id INTEGER REFERENCES staff(id),
            consultation_type VARCHAR(100),
            date DATE,
            time TIME,
            cc TEXT,
            hpi TEXT,
            pmh TEXT,
            pe TEXT,
            ros TEXT,
            allergies TEXT,
            family_history TEXT,
            social_history TEXT,
            diagnosis TEXT,
            treatment TEXT
        );
        """
    ]

    conn = None
    try:
        conn = connection()
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()

        print(" Done!!!")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_tables()
