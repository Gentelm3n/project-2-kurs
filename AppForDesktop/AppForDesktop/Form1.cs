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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            monthCalendar1.Visible = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "Hello Debils!";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void show_and_hidden_Calendar(object sender, EventArgs e)
        {
            monthCalendar1.Visible = !monthCalendar1.Visible;
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void submit_button(object sender, EventArgs e)
        {
            string subject = textBox1.Text;
            label2.Text = subject;
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }
    }
}
