using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

            
namespace AppForDesktop
{
    public partial class mainForm : Form
    {
        DateTime firstDateUpWeek = new DateTime(2025, 9, 1);

        public mainForm()
        {
            InitializeComponent();


            if ((date.Value - firstDateUpWeek).TotalDays / 7 % 2 == 0)
            {
                upDownWeek.Text = "Вы на верхней неделе";
            }
            else {
                upDownWeek.Text = "Вы на нижней неделе";
            }
            string[] arrTeach = { };
            string[] arrDisc = {};
            string[] arrAud = {};
            string[] arrCorp = {};
            string[,,] arrMain = new string[7, 14, 4];
            Label[,] arrLabel = { { labelDisc11, labelProf11, labelAud11, labelCorp11 }, { labelDisc12, labelProf12, labelAud12, labelCorp12 },
                                   { labelDisc21, labelProf21, labelAud21, labelCorp21 }, { labelDisc22, labelProf22, labelAud22, labelCorp22 },
                                   { labelDisc31, labelProf31, labelAud31, labelCorp31 }, { labelDisc32, labelProf32, labelAud32, labelCorp32 },
                                   { labelDisc41, labelProf41, labelAud41, labelCorp41 }, { labelDisc42, labelProf42, labelAud42, labelCorp42 },
                                   { labelDisc51, labelProf51, labelAud51, labelCorp51 }, { labelDisc52, labelProf52, labelAud52, labelCorp52 },
                                   { labelDisc61, labelProf61, labelAud61, labelCorp61 }, { labelDisc62, labelProf62, labelAud62, labelCorp62 },
                                   { labelDisc71, labelProf71, labelAud71, labelCorp71 }, { labelDisc72, labelProf72, labelAud72, labelCorp72 }
                                 };

            profCombo.Items.AddRange(arrTeach);
            subjectCombo.Items.AddRange(arrDisc);
            audCombo.Items.AddRange(arrAud);
            instCombo.Items.AddRange(arrCorp);
            

        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            string weekday = date.Value.DayOfWeek.ToString();

            if (((int) (date.Value - firstDateUpWeek).TotalDays) / 7 % 2 == 0)
            {
                upDownWeek.Text = "Вы на верхней неделе";
            }
            else
            {
                upDownWeek.Text = "Вы на нижней неделе";
            }

            switch (weekday)
            {
                case "Monday": Mon.Checked = true; break;
                case "Tuesday": Tue.Checked = true; break;
                case "Wednesday": Wed.Checked = true; break;
                case "Thursday": Thu.Checked = true; break;
                case "Friday": Fri.Checked = true; break;
                case "Saturday": Sat.Checked = true; break;
                case "Sunday": Sun.Checked = true; break;
            }
        }

        private void mainForm_Load(object sender, EventArgs e)
        {

        }

        private void changeDate(int i)
        {
            int weekday = (int) date.Value.DayOfWeek;

            if(weekday != 0)
            {
                weekday--;
            }
            else
            {
                weekday = 6;
            }
            DateTime realDate = date.Value.AddDays(-weekday+i);
            date.Value = realDate;
        }

        private void setLabel(int n, Label[,] arrLabel, string[,,] arrMain)
        {
            for(int i = 0; i < 14; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    arrLabel[i, j].Text = arrMain[n, i, j];
                }
            }
        }

        private void Mon_Click(object sender, EventArgs e)
        {
            changeDate(0);
        }

        private void Tue_Click(object sender, EventArgs e)
        {
            changeDate(1);
        }

        private void Wed_Click(object sender, EventArgs e)
        {
            changeDate(2);
        }

        private void Thu_Click(object sender, EventArgs e)
        {
            changeDate(3);
        }

        private void Fri_Click(object sender, EventArgs e)
        {
            changeDate(4);
        }

        private void Sat_Click(object sender, EventArgs e)
        {
            changeDate(5);
        }

        private void Sun_Click(object sender, EventArgs e)
        {
            changeDate(6);
        }

    }
}
