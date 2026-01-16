import { useState, useEffect } from 'react';
import { api, Profile, Project } from './api';

function App() {
    const [profile, setProfile] = useState<Profile | null>(null);
    const [filteredProjects, setFilteredProjects] = useState<Project[]>([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [selectedSkill, setSelectedSkill] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        loadProfile();
    }, []);

    useEffect(() => {
        if (selectedSkill) {
            loadProjectsBySkill(selectedSkill);
        } else if (profile) {
            setFilteredProjects(profile.projects);
        }
    }, [selectedSkill, profile]);

    const loadProfile = async () => {
        try {
            setLoading(true);
            const data = await api.getProfile();
            setProfile(data);
            setFilteredProjects(data.projects);
            setError(null);
        } catch (err) {
            setError('Failed to load profile. Make sure the backend is running.');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const loadProjectsBySkill = async (skill: string) => {
        try {
            const data = await api.getProjects(skill);
            setFilteredProjects(data.projects);
        } catch (err) {
            console.error('Failed to filter projects:', err);
        }
    };

    const handleSearch = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!searchQuery.trim()) {
            if (profile) setFilteredProjects(profile.projects);
            return;
        }

        try {
            const data = await api.search(searchQuery);
            setFilteredProjects(data.results.projects);
        } catch (err) {
            console.error('Search failed:', err);
        }
    };

    const handleSkillClick = (skillName: string) => {
        if (selectedSkill === skillName) {
            setSelectedSkill(null);
        } else {
            setSelectedSkill(skillName);
            setSearchQuery('');
        }
    };

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center">
                <div className="text-center">
                    <div className="inline-block animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-white"></div>
                    <p className="mt-4 text-white text-xl font-medium">Loading profile...</p>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center p-4">
                <div className="card max-w-md text-center">
                    <div className="text-6xl mb-4">⚠️</div>
                    <h2 className="text-2xl font-bold text-gray-800 mb-2">Connection Error</h2>
                    <p className="text-gray-600 mb-4">{error}</p>
                    <button onClick={loadProfile} className="btn-primary">
                        Retry
                    </button>
                </div>
            </div>
        );
    }

    if (!profile) return null;

    return (
        <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <header className="card mb-8 text-center">
                    <h1 className="text-5xl font-bold bg-gradient-to-r from-primary-600 to-purple-600 bg-clip-text text-transparent mb-2">
                        {profile.name}
                    </h1>
                    <p className="text-xl text-gray-600 mb-2">{profile.bio}</p>
                    <div className="flex items-center justify-center gap-4 text-gray-500 mb-4">
                        <span className="flex items-center gap-1">
                            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                            {profile.email}
                        </span>
                        <span className="flex items-center gap-1">
                            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            {profile.location}
                        </span>
                    </div>

                    {/* Social Links */}
                    <div className="flex justify-center gap-4">
                        {profile.links.map((link, idx) => (
                            <a
                                key={idx}
                                href={link.url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-primary-600 hover:text-primary-700 transition-colors duration-200 font-medium capitalize"
                            >
                                {link.platform}
                            </a>
                        ))}
                    </div>
                </header>

                {/* Search Bar */}
                <div className="card mb-8">
                    <form onSubmit={handleSearch} className="flex gap-3">
                        <input
                            type="text"
                            placeholder="Search projects, skills..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="input-field flex-1"
                        />
                        <button type="submit" className="btn-primary">
                            Search
                        </button>
                    </form>
                </div>

                {/* Skills Section */}
                <section className="card mb-8">
                    <h2 className="text-3xl font-bold text-gray-800 mb-4">Skills</h2>
                    <div className="flex flex-wrap gap-3">
                        {profile.skills.map((skill) => (
                            <button
                                key={skill.id}
                                onClick={() => handleSkillClick(skill.name)}
                                className={`badge cursor-pointer ${selectedSkill === skill.name
                                        ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white'
                                        : ''
                                    }`}
                            >
                                {skill.name}
                            </button>
                        ))}
                    </div>
                    {selectedSkill && (
                        <p className="mt-4 text-sm text-gray-600">
                            Showing projects using <strong>{selectedSkill}</strong>
                        </p>
                    )}
                </section>

                {/* Projects Section */}
                <section className="mb-8">
                    <h2 className="text-3xl font-bold text-white mb-6">
                        Projects {filteredProjects.length > 0 && `(${filteredProjects.length})`}
                    </h2>
                    {filteredProjects.length === 0 ? (
                        <div className="card text-center py-12">
                            <p className="text-gray-500 text-lg">No projects found matching your criteria.</p>
                        </div>
                    ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {filteredProjects.map((project) => (
                                <div key={project.id} className="card">
                                    <h3 className="text-xl font-bold text-gray-800 mb-2">{project.title}</h3>
                                    <p className="text-gray-600 mb-4">{project.description}</p>

                                    <div className="mb-4">
                                        <p className="text-sm font-semibold text-gray-700 mb-2">Technologies:</p>
                                        <div className="flex flex-wrap gap-2">
                                            {project.technologies.map((tech, idx) => (
                                                <span key={idx} className="badge text-xs">
                                                    {tech}
                                                </span>
                                            ))}
                                        </div>
                                    </div>

                                    {project.links.length > 0 && (
                                        <div className="flex gap-3 pt-4 border-t border-gray-200">
                                            {project.links.map((link, idx) => (
                                                <a
                                                    key={idx}
                                                    href={link.url}
                                                    target="_blank"
                                                    rel="noopener noreferrer"
                                                    className="text-primary-600 hover:text-primary-700 text-sm font-medium capitalize transition-colors duration-200"
                                                >
                                                    {link.platform} →
                                                </a>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            ))}
                        </div>
                    )}
                </section>

                {/* Experience Section */}
                <section className="card mb-8">
                    <h2 className="text-3xl font-bold text-gray-800 mb-6">Work Experience</h2>
                    <div className="space-y-6">
                        {profile.work.map((work) => (
                            <div key={work.id} className="border-l-4 border-primary-500 pl-4">
                                <h3 className="text-xl font-bold text-gray-800">{work.position}</h3>
                                <p className="text-primary-600 font-medium">{work.company}</p>
                                <p className="text-sm text-gray-500 mb-2">
                                    {work.start_date} - {work.end_date || 'Present'}
                                </p>
                                <p className="text-gray-700">{work.description}</p>
                            </div>
                        ))}
                    </div>
                </section>

                {/* Education Section */}
                <section className="card">
                    <h2 className="text-3xl font-bold text-gray-800 mb-6">Education</h2>
                    <div className="space-y-4">
                        {profile.education.map((edu) => (
                            <div key={edu.id} className="border-l-4 border-purple-500 pl-4">
                                <h3 className="text-xl font-bold text-gray-800">{edu.degree}</h3>
                                <p className="text-purple-600 font-medium">{edu.institution}</p>
                                <p className="text-sm text-gray-600">{edu.field_of_study}</p>
                                <p className="text-sm text-gray-500">
                                    {edu.start_date} - {edu.end_date || 'Present'}
                                </p>
                            </div>
                        ))}
                    </div>
                </section>
            </div>
        </div>
    );
}

export default App;
