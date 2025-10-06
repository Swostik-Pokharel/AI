
```dataviewjs
// ADD MORE SUBJECTS HERE - just add to this list
const subjects = [
    { name: "Calculus", page: "Calculus", emoji: "" },
    { name: "Linear Algebra", page: "Linear Algebra", emoji: "" },
    { name: "Statistics and probability", page: "Statistics and probability", emoji: "" },
    { name: "optimization", page: "optimization", emoji: "" },
    { name: "Discrete Maths", page: "disc", emoji: "" },
];

// Calculate progress for all subjects
let totalTasks = 0;
let totalCompleted = 0;
const subjectProgress = [];

subjects.forEach(subject => {
    const page = dv.page(subject.page);
    const tasks = page ? page.file.tasks : [];
    const total = tasks.length;
    const completed = tasks.filter(t => t.completed).length;
    const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;
    
    subjectProgress.push({
        name: subject.name,
        emoji: subject.emoji,
        page: subject.page,
        total: total,
        completed: completed,
        percentage: percentage
    });
    
    totalTasks += total;
    totalCompleted += completed;
});

const masterPercentage = totalTasks > 0 ? Math.round((totalCompleted / totalTasks) * 100) : 0;

// Progress bar functions
function createMasterBar(percentage) {
    const barLength = 100;
    const filledBars = Math.round((percentage / 100) * barLength);
    const emptyBars = barLength - filledBars;
    return "█".repeat(filledBars) + "░".repeat(emptyBars);
}

function createSubjectBar(percentage) {
    const barLength = 100;
    const filledBars = Math.round((percentage / 100) * barLength);
    const emptyBars = barLength - filledBars;
    return "█".repeat(filledBars) + "░".repeat(emptyBars);
}

// Display Master Progress
dv.paragraph(`## Overall Progress: ${totalCompleted}/${totalTasks} (${masterPercentage}%)`);
dv.paragraph(`\`${createMasterBar(masterPercentage)} ${masterPercentage}%\``);
dv.paragraph("---");

// Display all subjects with clickable links
subjectProgress.forEach(subject => {
    dv.paragraph(`**${subject.emoji} [[${subject.page}|${subject.name}]]:** ${subject.completed}/${subject.total} (${subject.percentage}%) \`${createSubjectBar(subject.percentage)} ${subject.percentage}%\``);
});
```


---
