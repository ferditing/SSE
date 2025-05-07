// frontend/src/pages/Catalog.jsx
import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Catalog() {
  const [courses, setCourses] = useState([]);
  const [enrolledIds, setEnrolledIds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // grab JWT from localStorage
  const token = localStorage.getItem("access_token");

  useEffect(() => {
    // 1) Fetch all courses
    axios
      .get("http://127.0.0.1:8000/api/courses", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => {
        setCourses(res.data);
      })
      .catch((err) => {
        console.error(err);
        setError("Failed to load courses");
      })
      .finally(() => {
        setLoading(false);
      });
  }, [token]);

  const handleEnroll = (courseId) => {
    // 2) Enroll in a course
    axios
      .post(
        "http://127.0.0.1:8000/api/enrollments",
        { course_id: courseId },
        { headers: { Authorization: `Bearer ${token}` } }
      )
      .then(() => {
        // Add this course to enrolledIds so button updates
        setEnrolledIds((prev) => [...prev, courseId]);
      })
      .catch((err) => {
        console.error(err);
        // you could set a per-course error state here
      });
  };

  if (loading) return <p>Loading courses…</p>;
  if (error) return <p className="text-red-500">{error}</p>;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
      {courses.map((course) => (
        <div
          key={course.id}
          className="border rounded-lg p-4 shadow-sm flex flex-col justify-between"
        >
          <div>
            <h2 className="text-xl font-semibold">{course.title}</h2>
            <p className="mt-2 text-gray-700">{course.description}</p>
          </div>
          <button
            className="mt-4 px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
            onClick={() => handleEnroll(course.id)}
            disabled={enrolledIds.includes(course.id)}
          >
            {enrolledIds.includes(course.id) ? "Enrolled!" : "Enroll"}
          </button>
        </div>
      ))}
    </div>
  );
}
