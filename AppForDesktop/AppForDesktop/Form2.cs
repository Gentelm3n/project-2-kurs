using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AppForDesktop
{
    public partial class AuthForm : Form
    {
        public AuthForm()
        {
            var corp = new List<string>();
            //try
            //{
            //    HttpClient client = new HttpClient();

            //    HttpResponseMessage response = await client.GetAsync("localhost:8080/getcorp");

            //if (response.IsSuccessStatusCode)
            //{
            string responseBody = "ИНОЗ, ФВТ";
            corp = responseBody.Split(',').ToList();
            Console.WriteLine($"Ответ: {responseBody}");
            //}
            //}
            //catch (Exception ex)
            //{
            //    Console.WriteLine($"Ошибка: {ex.Message}");
            //}
            //
            InitializeComponent();
            comboBox1.Items.AddRange(corp.ToArray());
            
        }

        private void AuthButton_Click(object sender, EventArgs e)
        {
            AppForDesktop.Program.SetCorp(comboBox1.Text);
            this.Close();
        }
    }
}
