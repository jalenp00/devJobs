interface CreateJob {
    title: string,
    company: string,
    techStack: string[] | null,
    location: string,
    type: string | null,
    contract: boolean | null,
    daysInOffice: Number | null,
    minSalary: Number | null,
    maxSalary: Number | null,
    yearsNeeded: Number | null,
    description: string
};

interface ResponseJob {
    id: string | number,
    title: string,
    company: string,
    techStack: string,
    datePosted: string,
    numApplicants: number,
    location: string,
    type: string,
    contract: boolean,
    daysInOffice: string | number,
    minSalary: Number,
    maxSalary: Number,
    yearsNeeded: number,
    description: string,
    numApplicants: Number
};