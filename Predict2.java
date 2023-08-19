package menu;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

@WebServlet(urlPatterns = {"/Predict"})
public class Predict2 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // test tampilan
        PrintWriter writer = resp.getWriter();
        writer.println("<html>");
        writer.println("<body>");
        writer.println("<h2> Prediksi Narkoba </h2>");
        //eksekusi file python
        ProcessBuilder processBuilder = new ProcessBuilder("python",
                "C:/Users/Revanza Zakly/IdeaProjects/Prediksi_Narkoba/hello.py");
        Process process = processBuilder.start();
        //Menampilkan hasil eksekusi
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null){
            writer.println("<h4>" + line + "</h4>");
            System.out.println(line);
        }
        writer.println("</body>");
        writer.println("</html>");
        writer.flush();

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doPost(req, resp);
    }
}
