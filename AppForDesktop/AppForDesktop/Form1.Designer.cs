namespace AppForDesktop
{
    partial class mainForm
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.date = new System.Windows.Forms.DateTimePicker();
            this.Mon = new System.Windows.Forms.RadioButton();
            this.Tue = new System.Windows.Forms.RadioButton();
            this.Wed = new System.Windows.Forms.RadioButton();
            this.Thu = new System.Windows.Forms.RadioButton();
            this.Fri = new System.Windows.Forms.RadioButton();
            this.Sat = new System.Windows.Forms.RadioButton();
            this.Sun = new System.Windows.Forms.RadioButton();
            this.label1para = new System.Windows.Forms.Label();
            this.labelTime11 = new System.Windows.Forms.Label();
            this.labelTime12 = new System.Windows.Forms.Label();
            this.labelTime22 = new System.Windows.Forms.Label();
            this.labelTime21 = new System.Windows.Forms.Label();
            this.label2para = new System.Windows.Forms.Label();
            this.labelTime42 = new System.Windows.Forms.Label();
            this.labelTime41 = new System.Windows.Forms.Label();
            this.label4para = new System.Windows.Forms.Label();
            this.labelTime32 = new System.Windows.Forms.Label();
            this.labelTime31 = new System.Windows.Forms.Label();
            this.label3para = new System.Windows.Forms.Label();
            this.labelTime62 = new System.Windows.Forms.Label();
            this.labelTime61 = new System.Windows.Forms.Label();
            this.label6para = new System.Windows.Forms.Label();
            this.labelTime52 = new System.Windows.Forms.Label();
            this.labelTime51 = new System.Windows.Forms.Label();
            this.label5para = new System.Windows.Forms.Label();
            this.groupWeekDay = new System.Windows.Forms.GroupBox();
            this.subjectCombo = new System.Windows.Forms.ComboBox();
            this.subjectLabel = new System.Windows.Forms.Label();
            this.instLabel = new System.Windows.Forms.Label();
            this.instCombo = new System.Windows.Forms.ComboBox();
            this.audLabel = new System.Windows.Forms.Label();
            this.audBox = new System.Windows.Forms.TextBox();
            this.profLabel = new System.Windows.Forms.Label();
            this.profCombo = new System.Windows.Forms.ComboBox();
            this.groupWeekDay.SuspendLayout();
            this.SuspendLayout();
            // 
            // date
            // 
            this.date.Location = new System.Drawing.Point(389, 34);
            this.date.Name = "date";
            this.date.Size = new System.Drawing.Size(215, 20);
            this.date.TabIndex = 7;
            this.date.ValueChanged += new System.EventHandler(this.dateTimePicker1_ValueChanged);
            // 
            // Mon
            // 
            this.Mon.AutoSize = true;
            this.Mon.Location = new System.Drawing.Point(15, 19);
            this.Mon.Name = "Mon";
            this.Mon.Size = new System.Drawing.Size(39, 17);
            this.Mon.TabIndex = 8;
            this.Mon.TabStop = true;
            this.Mon.Text = "Пн";
            this.Mon.UseVisualStyleBackColor = true;
            this.Mon.Click += new System.EventHandler(this.Mon_Click);
            // 
            // Tue
            // 
            this.Tue.AutoSize = true;
            this.Tue.Location = new System.Drawing.Point(60, 19);
            this.Tue.Name = "Tue";
            this.Tue.Size = new System.Drawing.Size(37, 17);
            this.Tue.TabIndex = 9;
            this.Tue.TabStop = true;
            this.Tue.Text = "Вт";
            this.Tue.UseVisualStyleBackColor = true;
            this.Tue.Click += new System.EventHandler(this.Tue_Click);
            // 
            // Wed
            // 
            this.Wed.AutoSize = true;
            this.Wed.Location = new System.Drawing.Point(103, 19);
            this.Wed.Name = "Wed";
            this.Wed.Size = new System.Drawing.Size(38, 17);
            this.Wed.TabIndex = 10;
            this.Wed.TabStop = true;
            this.Wed.Text = "Ср";
            this.Wed.UseVisualStyleBackColor = true;
            this.Wed.Click += new System.EventHandler(this.Wed_Click);
            // 
            // Thu
            // 
            this.Thu.AutoSize = true;
            this.Thu.Location = new System.Drawing.Point(147, 19);
            this.Thu.Name = "Thu";
            this.Thu.Size = new System.Drawing.Size(38, 17);
            this.Thu.TabIndex = 11;
            this.Thu.TabStop = true;
            this.Thu.Text = "Чт";
            this.Thu.UseVisualStyleBackColor = true;
            this.Thu.Click += new System.EventHandler(this.Thu_Click);
            // 
            // Fri
            // 
            this.Fri.AutoSize = true;
            this.Fri.Location = new System.Drawing.Point(191, 19);
            this.Fri.Name = "Fri";
            this.Fri.Size = new System.Drawing.Size(38, 17);
            this.Fri.TabIndex = 12;
            this.Fri.TabStop = true;
            this.Fri.Text = "Пт";
            this.Fri.UseVisualStyleBackColor = true;
            this.Fri.Click += new System.EventHandler(this.Fri_Click);
            // 
            // Sat
            // 
            this.Sat.AutoSize = true;
            this.Sat.Location = new System.Drawing.Point(235, 19);
            this.Sat.Name = "Sat";
            this.Sat.Size = new System.Drawing.Size(38, 17);
            this.Sat.TabIndex = 13;
            this.Sat.TabStop = true;
            this.Sat.Text = "Сб";
            this.Sat.UseVisualStyleBackColor = true;
            this.Sat.Click += new System.EventHandler(this.Sat_Click);
            // 
            // Sun
            // 
            this.Sun.AutoSize = true;
            this.Sun.Location = new System.Drawing.Point(279, 19);
            this.Sun.Name = "Sun";
            this.Sun.Size = new System.Drawing.Size(38, 17);
            this.Sun.TabIndex = 14;
            this.Sun.TabStop = true;
            this.Sun.Text = "Вс";
            this.Sun.UseVisualStyleBackColor = true;
            this.Sun.Click += new System.EventHandler(this.Sun_Click);
            // 
            // label1para
            // 
            this.label1para.AutoSize = true;
            this.label1para.Location = new System.Drawing.Point(13, 100);
            this.label1para.Name = "label1para";
            this.label1para.Size = new System.Drawing.Size(40, 13);
            this.label1para.TabIndex = 15;
            this.label1para.Text = "1 пара";
            // 
            // labelTime11
            // 
            this.labelTime11.AutoSize = true;
            this.labelTime11.Location = new System.Drawing.Point(53, 70);
            this.labelTime11.Name = "labelTime11";
            this.labelTime11.Size = new System.Drawing.Size(28, 13);
            this.labelTime11.TabIndex = 22;
            this.labelTime11.Text = "8:00";
            // 
            // labelTime12
            // 
            this.labelTime12.AutoSize = true;
            this.labelTime12.Location = new System.Drawing.Point(53, 130);
            this.labelTime12.Name = "labelTime12";
            this.labelTime12.Size = new System.Drawing.Size(28, 13);
            this.labelTime12.TabIndex = 23;
            this.labelTime12.Text = "8:50";
            // 
            // labelTime22
            // 
            this.labelTime22.AutoSize = true;
            this.labelTime22.Location = new System.Drawing.Point(53, 230);
            this.labelTime22.Name = "labelTime22";
            this.labelTime22.Size = new System.Drawing.Size(34, 13);
            this.labelTime22.TabIndex = 26;
            this.labelTime22.Text = "10:40";
            // 
            // labelTime21
            // 
            this.labelTime21.AutoSize = true;
            this.labelTime21.Location = new System.Drawing.Point(53, 170);
            this.labelTime21.Name = "labelTime21";
            this.labelTime21.Size = new System.Drawing.Size(28, 13);
            this.labelTime21.TabIndex = 25;
            this.labelTime21.Text = "9:50";
            // 
            // label2para
            // 
            this.label2para.AutoSize = true;
            this.label2para.Location = new System.Drawing.Point(13, 200);
            this.label2para.Name = "label2para";
            this.label2para.Size = new System.Drawing.Size(40, 13);
            this.label2para.TabIndex = 24;
            this.label2para.Text = "2 пара";
            // 
            // labelTime42
            // 
            this.labelTime42.AutoSize = true;
            this.labelTime42.Location = new System.Drawing.Point(53, 430);
            this.labelTime42.Name = "labelTime42";
            this.labelTime42.Size = new System.Drawing.Size(34, 13);
            this.labelTime42.TabIndex = 32;
            this.labelTime42.Text = "14:35";
            // 
            // labelTime41
            // 
            this.labelTime41.AutoSize = true;
            this.labelTime41.Location = new System.Drawing.Point(53, 370);
            this.labelTime41.Name = "labelTime41";
            this.labelTime41.Size = new System.Drawing.Size(34, 13);
            this.labelTime41.TabIndex = 31;
            this.labelTime41.Text = "13:45";
            // 
            // label4para
            // 
            this.label4para.AutoSize = true;
            this.label4para.Location = new System.Drawing.Point(13, 400);
            this.label4para.Name = "label4para";
            this.label4para.Size = new System.Drawing.Size(40, 13);
            this.label4para.TabIndex = 30;
            this.label4para.Text = "4 пара";
            // 
            // labelTime32
            // 
            this.labelTime32.AutoSize = true;
            this.labelTime32.Location = new System.Drawing.Point(53, 330);
            this.labelTime32.Name = "labelTime32";
            this.labelTime32.Size = new System.Drawing.Size(34, 13);
            this.labelTime32.TabIndex = 29;
            this.labelTime32.Text = "12:15";
            // 
            // labelTime31
            // 
            this.labelTime31.AutoSize = true;
            this.labelTime31.Location = new System.Drawing.Point(53, 270);
            this.labelTime31.Name = "labelTime31";
            this.labelTime31.Size = new System.Drawing.Size(34, 13);
            this.labelTime31.TabIndex = 28;
            this.labelTime31.Text = "11:25";
            // 
            // label3para
            // 
            this.label3para.AutoSize = true;
            this.label3para.Location = new System.Drawing.Point(13, 300);
            this.label3para.Name = "label3para";
            this.label3para.Size = new System.Drawing.Size(40, 13);
            this.label3para.TabIndex = 27;
            this.label3para.Text = "3 пара";
            // 
            // labelTime62
            // 
            this.labelTime62.AutoSize = true;
            this.labelTime62.Location = new System.Drawing.Point(53, 630);
            this.labelTime62.Name = "labelTime62";
            this.labelTime62.Size = new System.Drawing.Size(34, 13);
            this.labelTime62.TabIndex = 38;
            this.labelTime62.Text = "18:30";
            // 
            // labelTime61
            // 
            this.labelTime61.AutoSize = true;
            this.labelTime61.Location = new System.Drawing.Point(53, 570);
            this.labelTime61.Name = "labelTime61";
            this.labelTime61.Size = new System.Drawing.Size(34, 13);
            this.labelTime61.TabIndex = 37;
            this.labelTime61.Text = "17:40";
            // 
            // label6para
            // 
            this.label6para.AutoSize = true;
            this.label6para.Location = new System.Drawing.Point(13, 600);
            this.label6para.Name = "label6para";
            this.label6para.Size = new System.Drawing.Size(40, 13);
            this.label6para.TabIndex = 36;
            this.label6para.Text = "6 пара";
            // 
            // labelTime52
            // 
            this.labelTime52.AutoSize = true;
            this.labelTime52.Location = new System.Drawing.Point(53, 530);
            this.labelTime52.Name = "labelTime52";
            this.labelTime52.Size = new System.Drawing.Size(34, 13);
            this.labelTime52.TabIndex = 35;
            this.labelTime52.Text = "16:40";
            // 
            // labelTime51
            // 
            this.labelTime51.AutoSize = true;
            this.labelTime51.Location = new System.Drawing.Point(53, 470);
            this.labelTime51.Name = "labelTime51";
            this.labelTime51.Size = new System.Drawing.Size(34, 13);
            this.labelTime51.TabIndex = 34;
            this.labelTime51.Text = "15:50";
            // 
            // label5para
            // 
            this.label5para.AutoSize = true;
            this.label5para.Location = new System.Drawing.Point(13, 500);
            this.label5para.Name = "label5para";
            this.label5para.Size = new System.Drawing.Size(40, 13);
            this.label5para.TabIndex = 33;
            this.label5para.Text = "5 пара";
            // 
            // groupWeekDay
            // 
            this.groupWeekDay.Controls.Add(this.Mon);
            this.groupWeekDay.Controls.Add(this.Tue);
            this.groupWeekDay.Controls.Add(this.Wed);
            this.groupWeekDay.Controls.Add(this.Thu);
            this.groupWeekDay.Controls.Add(this.Fri);
            this.groupWeekDay.Controls.Add(this.Sat);
            this.groupWeekDay.Controls.Add(this.Sun);
            this.groupWeekDay.Location = new System.Drawing.Point(16, 12);
            this.groupWeekDay.Name = "groupWeekDay";
            this.groupWeekDay.Size = new System.Drawing.Size(354, 42);
            this.groupWeekDay.TabIndex = 39;
            this.groupWeekDay.TabStop = false;
            this.groupWeekDay.Text = "День недели";
            // 
            // subjectCombo
            // 
            this.subjectCombo.FormattingEnabled = true;
            this.subjectCombo.Location = new System.Drawing.Point(670, 68);
            this.subjectCombo.Name = "subjectCombo";
            this.subjectCombo.Size = new System.Drawing.Size(483, 21);
            this.subjectCombo.TabIndex = 41;
            // 
            // subjectLabel
            // 
            this.subjectLabel.AutoSize = true;
            this.subjectLabel.Location = new System.Drawing.Point(667, 40);
            this.subjectLabel.Name = "subjectLabel";
            this.subjectLabel.Size = new System.Drawing.Size(70, 13);
            this.subjectLabel.TabIndex = 42;
            this.subjectLabel.Text = "Дисциплина";
            // 
            // instLabel
            // 
            this.instLabel.AutoSize = true;
            this.instLabel.Location = new System.Drawing.Point(667, 140);
            this.instLabel.Name = "instLabel";
            this.instLabel.Size = new System.Drawing.Size(53, 13);
            this.instLabel.TabIndex = 45;
            this.instLabel.Text = "Институт";
            // 
            // instCombo
            // 
            this.instCombo.FormattingEnabled = true;
            this.instCombo.Location = new System.Drawing.Point(670, 168);
            this.instCombo.Name = "instCombo";
            this.instCombo.Size = new System.Drawing.Size(483, 21);
            this.instCombo.TabIndex = 44;
            // 
            // audLabel
            // 
            this.audLabel.AutoSize = true;
            this.audLabel.Location = new System.Drawing.Point(667, 237);
            this.audLabel.Name = "audLabel";
            this.audLabel.Size = new System.Drawing.Size(60, 13);
            this.audLabel.TabIndex = 48;
            this.audLabel.Text = "Аудитория";
            // 
            // audBox
            // 
            this.audBox.Location = new System.Drawing.Point(667, 267);
            this.audBox.Name = "audBox";
            this.audBox.Size = new System.Drawing.Size(294, 20);
            this.audBox.TabIndex = 46;
            // 
            // profLabel
            // 
            this.profLabel.AutoSize = true;
            this.profLabel.Location = new System.Drawing.Point(667, 340);
            this.profLabel.Name = "profLabel";
            this.profLabel.Size = new System.Drawing.Size(86, 13);
            this.profLabel.TabIndex = 51;
            this.profLabel.Text = "Преподаватель";
            // 
            // profCombo
            // 
            this.profCombo.FormattingEnabled = true;
            this.profCombo.Location = new System.Drawing.Point(670, 368);
            this.profCombo.Name = "profCombo";
            this.profCombo.Size = new System.Drawing.Size(483, 21);
            this.profCombo.TabIndex = 50;
            // 
            // mainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1264, 681);
            this.Controls.Add(this.profLabel);
            this.Controls.Add(this.profCombo);
            this.Controls.Add(this.audLabel);
            this.Controls.Add(this.audBox);
            this.Controls.Add(this.instLabel);
            this.Controls.Add(this.instCombo);
            this.Controls.Add(this.subjectLabel);
            this.Controls.Add(this.subjectCombo);
            this.Controls.Add(this.groupWeekDay);
            this.Controls.Add(this.labelTime62);
            this.Controls.Add(this.labelTime61);
            this.Controls.Add(this.label6para);
            this.Controls.Add(this.labelTime52);
            this.Controls.Add(this.labelTime51);
            this.Controls.Add(this.label5para);
            this.Controls.Add(this.labelTime42);
            this.Controls.Add(this.labelTime41);
            this.Controls.Add(this.label4para);
            this.Controls.Add(this.labelTime32);
            this.Controls.Add(this.labelTime31);
            this.Controls.Add(this.label3para);
            this.Controls.Add(this.labelTime22);
            this.Controls.Add(this.labelTime21);
            this.Controls.Add(this.label2para);
            this.Controls.Add(this.labelTime12);
            this.Controls.Add(this.labelTime11);
            this.Controls.Add(this.label1para);
            this.Controls.Add(this.date);
            this.Name = "mainForm";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.mainForm_Load);
            this.groupWeekDay.ResumeLayout(false);
            this.groupWeekDay.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.DateTimePicker date;
        private System.Windows.Forms.RadioButton Mon;
        private System.Windows.Forms.RadioButton Tue;
        private System.Windows.Forms.RadioButton Wed;
        private System.Windows.Forms.RadioButton Thu;
        private System.Windows.Forms.RadioButton Fri;
        private System.Windows.Forms.RadioButton Sat;
        private System.Windows.Forms.RadioButton Sun;
        private System.Windows.Forms.Label label1para;
        private System.Windows.Forms.Label labelTime11;
        private System.Windows.Forms.Label labelTime12;
        private System.Windows.Forms.Label labelTime22;
        private System.Windows.Forms.Label labelTime21;
        private System.Windows.Forms.Label label2para;
        private System.Windows.Forms.Label labelTime42;
        private System.Windows.Forms.Label labelTime41;
        private System.Windows.Forms.Label label4para;
        private System.Windows.Forms.Label labelTime32;
        private System.Windows.Forms.Label labelTime31;
        private System.Windows.Forms.Label label3para;
        private System.Windows.Forms.Label labelTime62;
        private System.Windows.Forms.Label labelTime61;
        private System.Windows.Forms.Label label6para;
        private System.Windows.Forms.Label labelTime52;
        private System.Windows.Forms.Label labelTime51;
        private System.Windows.Forms.Label label5para;
        private System.Windows.Forms.GroupBox groupWeekDay;
        private System.Windows.Forms.ComboBox subjectCombo;
        private System.Windows.Forms.Label subjectLabel;
        private System.Windows.Forms.Label instLabel;
        private System.Windows.Forms.ComboBox instCombo;
        private System.Windows.Forms.Label audLabel;
        private System.Windows.Forms.TextBox audBox;
        private System.Windows.Forms.Label profLabel;
        private System.Windows.Forms.ComboBox profCombo;
    }
}

