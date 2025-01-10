from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="mAk_Octane123*$",
        database="survey_data"
    )

@app.route("/")
def display_view():
    # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        # Fetch data from the view
        cursor.execute("SELECT * FROM daily_summary")
        daily_summary = cursor.fetchall()

        cursor.execute("SELECT * FROM area_summary")
        area_summary = cursor.fetchall()

        cursor.execute("SELECT * FROM interviewer_summary")
        interviewer_summary = cursor.fetchall()

    except Exception as e:
        print(f"Error: {e}")
        daily_summary = interviewer_summary = area_summary = []

    finally:
        # Close the connection
        cursor.close()
        connection.close()

    # Render data in an HTML template
    return render_template("layout.html", 
                           daily_summary=daily_summary,
                            interviewer_summary=interviewer_summary,
                            enumeration_area_summary=area_summary,)

if __name__ == "__main__":
    app.run(debug=True)


