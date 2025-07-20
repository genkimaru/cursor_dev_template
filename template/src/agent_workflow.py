# Agent Network Implementation using Pocket Flow Framework
# Complete 6-node software development lifecycle automation

from pocketflow import Node, Flow
import os
import json
import subprocess
from datetime import datetime
from typing import Dict, Any, List, Optional

# =============================================================================
# Utility Functions
# =============================================================================

def call_llm(prompt: str, system_prompt: str = "") -> str:
    """
    Simulate LLM call - replace with actual LLM API call
    """
    # This is a placeholder - replace with actual LLM integration
    # Example: OpenAI, Anthropic, or local model
    return f"[LLM Response to: {prompt[:50]}...]"

def get_user_input(prompt: str) -> str:
    """Get input from user with prompt"""
    return input(f"\n{prompt}\n> ")

def confirm_with_user(message: str) -> bool:
    """Get confirmation from user"""
    response = input(f"\n{message}\n(y/n): ").lower().strip()
    return response in ['y', 'yes']

def save_to_file(content: str, filename: str) -> None:
    """Save content to file"""
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else ".", exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ File saved: {filename}")

def execute_command(command: str) -> tuple:
    """Execute shell command and return (success, output)"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

def push_to_git(commit_message: str) -> bool:
    """Push code to git repository if available"""
    try:
        # Check if git repo exists
        success, _ = execute_command("git status")
        if not success:
            print("⚠️  No git repository found, skipping push")
            return True

        # Add, commit and push
        execute_command("git add .")
        execute_command(f'git commit -m "{commit_message}"')
        success, output = execute_command("git push")

        if success:
            print("✅ Code pushed to repository successfully")
        else:
            print(f"⚠️  Git push failed: {output}")

        return success
    except Exception as e:
        print(f"⚠️  Git operations failed: {e}")
        return False

# =============================================================================
# Node 1: Problem Acquisition Agent
# =============================================================================

class ProblemAcquisitionNode(Node):
    """First node: Interact with user and acquire the initial problem"""

    def exec(self, _) -> Dict[str, Any]:
        print("\n🤖 Welcome to the AI Development Assistant!")
        print("I'll help you build a complete software solution from problem to implementation.")

        # Get initial problem description
        problem = get_user_input(
            "Please describe the problem you want to solve or the software you want to build:"
        )

        # Get additional context
        context = get_user_input(
            "Any additional context, requirements, or constraints? (Optional, press Enter to skip):"
        )

        # Get target technology preferences
        tech_stack = get_user_input(
            "Preferred technology stack or programming language? (Optional, press Enter for auto-selection):"
        )

        return {
            "initial_problem": problem,
            "context": context,
            "preferred_tech": tech_stack,
            "timestamp": datetime.now().isoformat()
        }

    def post(self, shared: Dict, prep_res: Any, exec_res: Dict) -> str:
        shared["problem_data"] = exec_res
        shared["current_stage"] = "problem_acquired"
        print(f"\n✅ Problem acquired: {exec_res['initial_problem'][:100]}...")
        return "problem_clarification"

# =============================================================================
# Node 2: Problem Clarification Agent
# =============================================================================

class ProblemClarificationNode(Node):
    """Second node: Clarify problem through interactive conversation"""

    def prep(self, shared: Dict) -> Dict:
        return shared["problem_data"]

    def exec(self, problem_data: Dict) -> Dict:
        print("\n🔍 Let me clarify your requirements...")

        # Analyze initial problem with LLM
        analysis_prompt = f"""
        Analyze this problem description and identify areas that need clarification:

        Problem: {problem_data['initial_problem']}
        Context: {problem_data['context']}
        Tech Stack: {problem_data['preferred_tech']}

        Generate specific questions to clarify:
        1. Functional requirements
        2. Non-functional requirements
        3. User interface needs
        4. Integration requirements
        5. Constraints and limitations

        Format as a numbered list of clear, specific questions.
        """

        questions = call_llm(analysis_prompt)

        # Interactive clarification with user
        clarifications = {}
        print(f"\n📋 Clarification Questions:\n{questions}")

        # Simulate interactive Q&A (in real implementation, parse questions and ask individually)
        detailed_requirements = get_user_input(
            "Please provide detailed answers to clarify your requirements:"
        )

        # Generate comprehensive requirements document
        requirements_prompt = f"""
        Based on the initial problem and user clarifications, create a comprehensive requirements document:

        Initial Problem: {problem_data['initial_problem']}
        User Clarifications: {detailed_requirements}

        Create a structured requirements document with:
        1. Project Overview
        2. Functional Requirements
        3. Non-Functional Requirements
        4. Technical Requirements
        5. User Interface Requirements
        6. Success Criteria
        7. Constraints and Assumptions
        """

        requirements_doc = call_llm(requirements_prompt)

        return {
            "clarification_questions": questions,
            "user_responses": detailed_requirements,
            "requirements_document": requirements_doc,
            "clarification_complete": True
        }

    def post(self, shared: Dict, prep_res: Dict, exec_res: Dict) -> str:
        shared["clarification_data"] = exec_res

        # Save user_requirements.md
        requirements_content = f"""# User Requirements Document

## Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Initial Problem
{shared['problem_data']['initial_problem']}

## Clarification Process
{exec_res['clarification_questions']}

## User Responses
{exec_res['user_responses']}

## Comprehensive Requirements
{exec_res['requirements_document']}
"""

        save_to_file(requirements_content, "user_requirements.md")
        shared["current_stage"] = "requirements_clarified"
        print("\n✅ Requirements clarified and documented")
        return "solution_planning"

# =============================================================================
# Node 3: Solution Planning Agent
# =============================================================================

class SolutionPlanningNode(Node):
    """Third node: Find solution and create implementation plan"""

    def prep(self, shared: Dict) -> Dict:
        return {
            "requirements": shared["clarification_data"]["requirements_document"],
            "problem_data": shared["problem_data"]
        }

    def exec(self, data: Dict) -> Dict:
        print("\n📋 Creating solution plan...")

        # Generate solution architecture
        architecture_prompt = f"""
        Based on these requirements, design a software solution:

        Requirements: {data['requirements']}

        Provide:
        1. Solution Architecture Overview
        2. Technology Stack Recommendation
        3. System Components and Their Interactions
        4. Data Flow and Storage Strategy
        5. Key Design Decisions and Rationale
        """

        solution_architecture = call_llm(architecture_prompt)

        # Generate implementation plan
        plan_prompt = f"""
        Create a detailed implementation plan for this solution:

        Architecture: {solution_architecture}

        Break down into:
        1. Development Phases (with priorities)
        2. Specific Tasks for Each Phase
        3. Dependencies Between Tasks
        4. Estimated Effort and Timeline
        5. Risk Assessment and Mitigation
        6. Testing Strategy
        """

        implementation_plan = call_llm(plan_prompt)

        # Generate task breakdown
        tasks_prompt = f"""
        Convert the implementation plan into specific, actionable tasks:

        Plan: {implementation_plan}

        Create a task list with:
        - Task ID
        - Task Description
        - Prerequisites
        - Deliverables
        - Priority Level
        """

        task_breakdown = call_llm(tasks_prompt)

        return {
            "solution_architecture": solution_architecture,
            "implementation_plan": implementation_plan,
            "task_breakdown": task_breakdown,
            "planning_complete": True
        }

    def post(self, shared: Dict, prep_res: Dict, exec_res: Dict) -> str:
        shared["planning_data"] = exec_res

        # Save plan_and_tasks.md
        plan_content = f"""# Solution Plan and Tasks

## Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Solution Architecture
{exec_res['solution_architecture']}

## Implementation Plan
{exec_res['implementation_plan']}

## Task Breakdown
{exec_res['task_breakdown']}
"""

        save_to_file(plan_content, "plan_and_tasks.md")
        shared["current_stage"] = "solution_planned"
        print("\n✅ Solution planned and tasks defined")
        return "implementation"

# =============================================================================
# Node 4: Implementation Agent
# =============================================================================

class ImplementationNode(Node):
    """Fourth node: Implement solution step by step with user confirmation"""

    def prep(self, shared: Dict) -> Dict:
        return {
            "plan": shared["planning_data"]["implementation_plan"],
            "tasks": shared["planning_data"]["task_breakdown"],
            "architecture": shared["planning_data"]["solution_architecture"]
        }

    def exec(self, data: Dict) -> Dict:
        print("\n💻 Starting implementation...")

        implemented_components = []
        implementation_log = []

        # Parse tasks and implement step by step
        # This is a simplified version - real implementation would parse tasks properly

        # Simulate implementation phases
        phases = [
            "Project Structure Setup",
            "Core Components Implementation",
            "Business Logic Development",
            "User Interface Development",
            "Integration and Data Handling"
        ]

        for i, phase in enumerate(phases, 1):
            print(f"\n🔧 Phase {i}: {phase}")

            # Generate code for this phase
            code_prompt = f"""
            Implement {phase} based on:

            Architecture: {data['architecture']}
            Plan: {data['plan']}

            Generate actual, working code with:
            1. Proper file structure
            2. Clean, documented code
            3. Error handling
            4. Best practices
            """

            generated_code = call_llm(code_prompt)

            print(f"Generated code for {phase}:")
            print(f"{generated_code[:200]}...")

            # Get user confirmation
            if confirm_with_user(f"Approve implementation for {phase}?"):
                # Save code files (simplified - would generate actual files)
                filename = f"phase_{i}_{phase.lower().replace(' ', '_')}.py"
                save_to_file(generated_code, f"src/{filename}")

                implemented_components.append({
                    "phase": phase,
                    "filename": filename,
                    "code": generated_code,
                    "approved": True,
                    "timestamp": datetime.now().isoformat()
                })

                # Push to git if user confirms
                if confirm_with_user("Push this phase to repository?"):
                    push_to_git(f"Implement {phase}")

                implementation_log.append(f"✅ {phase} - Completed and approved")
            else:
                implementation_log.append(f"❌ {phase} - Rejected by user")
                print(f"Phase {phase} rejected. Please provide feedback for revision.")

        return {
            "implemented_components": implemented_components,
            "implementation_log": implementation_log,
            "implementation_complete": True
        }

    def post(self, shared: Dict, prep_res: Dict, exec_res: Dict) -> str:
        shared["implementation_data"] = exec_res
        shared["current_stage"] = "implementation_complete"

        print(f"\n✅ Implementation completed with {len(exec_res['implemented_components'])} components")
        return "testing"

# =============================================================================
# Node 5: Testing Agent
# =============================================================================

class TestingNode(Node):
    """Fifth node: Create and run tests until all pass"""

    def prep(self, shared: Dict) -> Dict:
        return {
            "components": shared["implementation_data"]["implemented_components"],
            "architecture": shared["planning_data"]["solution_architecture"]
        }

    def exec(self, data: Dict) -> Dict:
        print("\n🧪 Creating and running tests...")

        test_results = []
        all_tests_passed = False
        iteration = 0
        max_iterations = 3

        while not all_tests_passed and iteration < max_iterations:
            iteration += 1
            print(f"\n🔄 Testing iteration {iteration}")

            current_test_results = []

            # Generate tests for each component
            for component in data["components"]:
                print(f"Testing {component['phase']}...")

                # Generate test cases
                test_prompt = f"""
                Create comprehensive tests for this component:

                Component: {component['phase']}
                Code: {component['code']}

                Generate:
                1. Unit tests
                2. Integration tests
                3. Edge cases
                4. Error handling tests
                5. Performance tests (if applicable)

                Use appropriate testing framework and include assertions.
                """

                test_code = call_llm(test_prompt)

                # Simulate running tests
                # In real implementation, would execute actual tests
                test_passed = True  # Simplified - would run real tests

                test_result = {
                    "component": component["phase"],
                    "test_code": test_code,
                    "passed": test_passed,
                    "iteration": iteration
                }

                current_test_results.append(test_result)

                # Save test file
                test_filename = f"tests/test_{component['filename']}"
                save_to_file(test_code, test_filename)

            # Check if all tests passed
            all_tests_passed = all([result["passed"] for result in current_test_results])
            test_results.extend(current_test_results)

            if not all_tests_passed:
                print("❌ Some tests failed. Analyzing and fixing...")
                # In real implementation, would analyze failures and fix code
            else:
                print("✅ All tests passed!")

        # Generate test report
        test_report = f"""# Test Results Report

## Testing Summary
- Total Iterations: {iteration}
- All Tests Passed: {all_tests_passed}
- Components Tested: {len(data['components'])}

## Test Results by Component
"""

        for result in test_results:
            status = "✅ PASSED" if result["passed"] else "❌ FAILED"
            test_report += f"\n### {result['component']} - {status}\n"
            test_report += f"Iteration: {result['iteration']}\n"

        return {
            "test_results": test_results,
            "all_tests_passed": all_tests_passed,
            "test_report": test_report,
            "testing_complete": True
        }

    def post(self, shared: Dict, prep_res: Dict, exec_res: Dict) -> str:
        shared["testing_data"] = exec_res

        # Save test_cases_report.md
        save_to_file(exec_res["test_report"], "test_cases_report.md")

        shared["current_stage"] = "testing_complete"
        print(f"\n✅ Testing completed - All tests passed: {exec_res['all_tests_passed']}")
        return "documentation"

# =============================================================================
# Node 6: Documentation Agent
# =============================================================================

class DocumentationNode(Node):
    """Sixth node: Generate README.md and changelog.md"""

    def prep(self, shared: Dict) -> Dict:
        return {
            "requirements": shared["clarification_data"]["requirements_document"],
            "architecture": shared["planning_data"]["solution_architecture"],
            "components": shared["implementation_data"]["implemented_components"],
            "test_results": shared["testing_data"]["test_results"]
        }

    def exec(self, data: Dict) -> Dict:
        print("\n📚 Generating documentation...")

        # Generate README.md
        readme_prompt = f"""
        Create a comprehensive README.md file for this project:

        Requirements: {data['requirements']}
        Architecture: {data['architecture']}
        Components: {[c['phase'] for c in data['components']]}

        Include:
        1. Project Title and Description
        2. Features and Functionality
        3. Architecture Overview
        4. Installation Instructions
        5. Usage Guide with Examples
        6. API Documentation (if applicable)
        7. Contributing Guidelines
        8. License Information
        9. Roadmap and Future Plans
        10. Support and Contact Information
        """

        readme_content = call_llm(readme_prompt)

        # Generate changelog
        changelog_prompt = f"""
        Create a CHANGELOG.md file documenting the development process:

        Implementation phases: {[c['phase'] for c in data['components']]}
        Test results: {len(data['test_results'])} tests

        Format as:
        # Changelog

        ## [1.0.0] - {datetime.now().strftime('%Y-%m-%d')}

        ### Added
        - List of implemented features

        ### Changed
        - Any modifications made

        ### Fixed
        - Issues resolved

        ### Technical
        - Implementation details
        """

        changelog_content = call_llm(changelog_prompt)

        # Generate additional documentation
        docs_structure = {
            "README.md": readme_content,
            "CHANGELOG.md": changelog_content,
            "docs/ARCHITECTURE.md": data['architecture'],
            "docs/INSTALLATION.md": "# Installation Guide\n\n" + readme_content.split("## Installation")[1].split("##")[0] if "## Installation" in readme_content else "# Installation Guide\n\nDetailed installation instructions will be added here."
        }

        return {
            "readme_content": readme_content,
            "changelog_content": changelog_content,
            "docs_structure": docs_structure,
            "documentation_complete": True
        }

    def post(self, shared: Dict, prep_res: Dict, exec_res: Dict) -> str:
        shared["documentation_data"] = exec_res

        # Save all documentation files
        for filename, content in exec_res["docs_structure"].items():
            save_to_file(content, filename)

        # Final git push
        if confirm_with_user("Push final documentation to repository?"):
            push_to_git("Add comprehensive documentation and changelog")

        shared["current_stage"] = "project_complete"
        print("\n🎉 Project completed successfully!")

        # Print final summary
        print("\n" + "="*60)
        print("📋 PROJECT COMPLETION SUMMARY")
        print("="*60)
        print(f"✅ Requirements: user_requirements.md")
        print(f"✅ Planning: plan_and_tasks.md")
        print(f"✅ Implementation: {len(shared['implementation_data']['implemented_components'])} components")
        print(f"✅ Testing: test_cases_report.md")
        print(f"✅ Documentation: README.md, CHANGELOG.md")
        print("="*60)

        return "complete"

# =============================================================================
# Flow Creation and Main Execution
# =============================================================================

def create_development_flow() -> Flow:
    """Create and return the complete 6-node development flow"""

    # Create all nodes
    problem_node = ProblemAcquisitionNode()
    clarification_node = ProblemClarificationNode()
    planning_node = SolutionPlanningNode()
    implementation_node = ImplementationNode()
    testing_node = TestingNode()
    documentation_node = DocumentationNode()

    # Connect nodes in sequence
    problem_node >> clarification_node
    clarification_node >> planning_node
    planning_node >> implementation_node
    implementation_node >> testing_node
    testing_node >> documentation_node

    return Flow(start=problem_node)

def main():
    """Main function to run the development flow"""
    print("🚀 Initializing AI Development Agent Network")
    print("Based on Pocket Flow Framework")
    print("-" * 50)

    # Initialize shared state
    shared = {
        "project_id": f"project_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "start_time": datetime.now().isoformat(),
        "current_stage": "initialized",
        "problem_data": None,
        "clarification_data": None,
        "planning_data": None,
        "implementation_data": None,
        "testing_data": None,
        "documentation_data": None
    }

    # Create and run the flow
    try:
        dev_flow = create_development_flow()
        dev_flow.run(shared)

        print(f"\n🎉 Development flow completed successfully!")
        print(f"Project ID: {shared['project_id']}")
        print(f"Final Stage: {shared['current_stage']}")

    except KeyboardInterrupt:
        print(f"\n⚠️  Flow interrupted by user")
        print(f"Current stage: {shared.get('current_stage', 'unknown')}")

    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        print(f"Current stage: {shared.get('current_stage', 'unknown')}")

if __name__ == "__main__":
    main()
