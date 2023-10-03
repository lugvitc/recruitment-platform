## Linux Club Recruitment Management Platform

### Functions

- Portal for department wise application shortlisting.

- Search feature for finding record of any applicant.

- Ability to use filters to filter applicant records based on any criteria.

- Shortlisted applicants are automatically moved to a Slot Booking table which automatically generates credentials for them to login and use the [Linux Club Slot Booking Platform](https://github.com/lugvitc/lug-slotbooking)

### Instructions for Intial Setup

- Clone the repository.

- Open app.py and modify line 11 or 12 to setup the database connection.

- Install docker if you don't have it installed and run ```sudo docker compose up -d```

- Now open the database you configured and you will see that all the tables have been created.

- Open the admin table and create a record, you will need to use this credentials you added to admin table to login in to the platform.

- Import the complete applicant data into the All Candidates table. 

- Now you need to use SQL Queries to copy these records into department wise tables. We will give example MySQL queries here.

#### Moving Applicant Data to Department Tables

```sql
INSERT INTO technical__rec (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_linux_1`, `tech_linux_2`, `tech_linux_3`, `tech_linux_4`, `tech_linux_5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_linux_1`, `tech_linux_2`, `tech_linux_3`, `tech_linux_4`, `tech_linux_5`
FROM all__candidates
WHERE prefDept='Technical Department - Linux' or prefDept2='Technical Department - Linux';
```

```sql
INSERT INTO technical__frontend (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_frontend_1`, `tech_frontend_2`, `tech_frontend_3`, `tech_frontend_4`, `tech_frontend_5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_frontend_1`, `tech_frontend_2`, `tech_frontend_3`, `tech_frontend_4`, `tech_frontend_5`
FROM all__candidates
WHERE prefDept='Technical Department - Frontend' or prefDept2='Technical Department - Frontend';
```

```sql
INSERT INTO technical__backend (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_backend_1`, `tech_backend_2`, `tech_backend_3`, `tech_backend_4`, `tech_backend_5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_backend_1`, `tech_backend_2`, `tech_backend_3`, `tech_backend_4`, `tech_backend_5`
FROM all__candidates
WHERE prefDept='Technical Department - Backend' or prefDept2='Technical Department - Backend';
```

```sql
INSERT INTO technical__cybersec (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_cybersec_1`, `tech_cybersec_2`, `tech_cybersec_3`, `tech_cybersec_4`, `tech_cybersec_5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_cybersec_1`, `tech_cybersec_2`, `tech_cybersec_3`, `tech_cybersec_4`, `tech_cybersec_5`
FROM all__candidates
WHERE prefDept='Technical Department - Cybersec' or prefDept2='Technical Department - Cybersec';
```

```sql
INSERT INTO technical__devops (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_devops_1`, `tech_devops_2`, `tech_devops_3`, `tech_devops_4`, `tech_devops_5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `tech1`, `tech2`, `tech3`, `tech_devops_1`, `tech_devops_2`, `tech_devops_3`, `tech_devops_4`, `tech_devops_5`
FROM all__candidates
WHERE prefDept='Technical Department - DevOps' or prefDept2='Technical Department - DevOps';
```

```sql
INSERT INTO management (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `mang1`, `mang2`, `mang3`, `mang4`, `mang5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `mang1`, `mang2`, `mang3`, `mang4`, `mang5`
FROM all__candidates
WHERE prefDept='Management Department' or prefDept2='Management Department';
```

```sql
INSERT INTO operations (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `ops1`, `ops2`) SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `ops1`, `ops2` FROM all__candidates WHERE prefDept='Operations Department' or prefDept2='Operations Department';
```

```sql
INSERT INTO content (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `content1`, `content2`, `content3`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `content1`, `content2`, `content3`
FROM all__candidates
WHERE prefDept='Content Department' or prefDept2='Content Department';
```

```sql
NSERT INTO media (`id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `media1`, `media_photo_1`, `media_photo_2`, `media_photo_3`, `media_photo_4`, `media_photo_5`, `media_graphic_1`, `media_graphic_2`, `media_graphic_3`, `media_graphic_4`, `media_graphic_5`, `media_social_media_1`, `media_social_media_2`, `media_social_media_3`, `media_social_media_4`, `media_social_media_5`, `media_video_1`, `media_video_2`, `media_video_3`, `media_video_4`, `media_video_5`)
SELECT `id`, `name`, `email`, `contact`, `prefDept`, `prefDept2`, `regno`, `whatLinux`, `whyLinux`, `expLinux`, `media1`, `media_photo_1`, `media_photo_2`, `media_photo_3`, `media_photo_4`, `media_photo_5`, `media_graphic_1`, `media_graphic_2`, `media_graphic_3`, `media_graphic_4`, `media_graphic_5`, `media_social_media_1`, `media_social_media_2`, `media_social_media_3`, `media_social_media_4`, `media_social_media_5`, `media_video_1`, `media_video_2`, `media_video_3`, `media_video_4`, `media_video_5`
FROM all__candidates WHERE prefDept
LIKE 'Media%' OR prefDept2 LIKE 'Media%';
```

After all the above queries are executed, data will be moved to all the department wise tables from the All Candidates table.

Keep in mind that, the above queries are for the existing database structure. If you change the database structure in models.py, you need to make changes to these queries also.

### How to Use the Recruitment Management Platform ?

- Configure and deploy the platform following the above instructions.

- You can visit the web page on a browser and you will see a login screen.

- Login using the credentials you added to the admin table.

- You will be able to see all the applicant records on the All Candidates table.

- You can go to any department table and see the applicants who applied for that department.

- There you can shortlist any applicant.

- Once an applicant is shortlisted, there record will be automatically moved to the SlotBookedApplicants table and the shortlisted applicant will be able to login to the [interview slot booking platform](https://github.com/lugvitc/lug-slotbooking) using their reg no and phone number.

### Instructions for Contributing

- Fork the repository and clone the fork.

- Add improvements with clear documentation on what you added.

- Submit a pull request. 

- Linux Club Technical Team will review it and merge the pull request.



***If you face any issues or if you have any doubts, you can reach our support team at [Linux Club Forums](https://forum.lugvitc.org/)***
