const API_BASE_URL = (import.meta.env.VITE_API_URL || 'http://localhost:8000').replace(/\/$/, '');

export interface Profile {
    id: number;
    name: string;
    email: string;
    bio: string;
    location: string;
    skills: Skill[];
    projects: Project[];
    education: Education[];
    work: WorkExperience[];
    links: Link[];
}

export interface Skill {
    id: number;
    name: string;
}

export interface Project {
    id: number;
    title: string;
    description: string;
    technologies: string[];
    links: ProjectLink[];
}

export interface ProjectLink {
    platform: string;
    url: string;
}

export interface Education {
    id: number;
    institution: string;
    degree: string;
    field_of_study: string;
    start_date: string;
    end_date?: string;
}

export interface WorkExperience {
    id: number;
    company: string;
    position: string;
    description: string;
    start_date: string;
    end_date?: string;
}

export interface Link {
    platform: string;
    url: string;
}

export const api = {
    async getProfile(): Promise<Profile> {
        const response = await fetch(`${API_BASE_URL}/api/profile`);
        if (!response.ok) throw new Error('Failed to fetch profile');
        return response.json();
    },

    async getProjects(skill?: string): Promise<{ projects: Project[] }> {
        const url = skill
            ? `${API_BASE_URL}/api/projects?skill=${encodeURIComponent(skill)}`
            : `${API_BASE_URL}/api/projects`;
        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch projects');
        return response.json();
    },

    async search(query: string): Promise<{ query: string; results: { projects: Project[]; skills: Skill[] } }> {
        const response = await fetch(`${API_BASE_URL}/api/search?q=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error('Failed to search');
        return response.json();
    },

    async healthCheck(): Promise<{ status: string; message: string }> {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (!response.ok) throw new Error('Health check failed');
        return response.json();
    },
};
