# Best practices for writing Dockerfile

1. The Docker image should generate a container that can be stopped and destroyed, then rebuilt and replaced with an absolute minimum set up and configuration.

2. Use multi-stage builds when it is needed because it drastically reduces the final size of the image and perfectly uses caching of layers and stages. 

3. Reduce attack surface
    * Use `.dockerignore` file to exclude not relevant files from build context.
    * In a multistage build, you can create an intermediate container from which you can copy only the resulting artifacts to the final image.
    * Use trusted and maintained images to reduce number of vulnerabilities and problems.
    * Update images frequently as new security vulnerabilities are discovered every day.
    * Expose only those ports that application needs.

4. Don’t install unnecessary packages to reduce complexity, dependencies, file sizes, and build times.

5. Minimize the number of layers by grouping `RUN`, `COPY` and `ADD` instructions. Other instructions do not increase the size of build.

6. Sort multi-line arguments alphanumerically for the ease to maintain and update.

    Example:
    ``` Dockerfile
    RUN apt-get update && apt-get -y install \
    curl \
    sudo \
    wget
    ```
7. Place Docker layers in such order to maximize build cache.

8. Avoid unnecessary privileges
    * Avoid using root user to run the container. There are a few use cases when the container needs to be executed by root, so try to use `USER` instruction to change the default UID from 0 to a rootless user.

    * Make executables owned by root and not writable. This will block the executing user from modifying existing binaries or scripts, which could enable different attacks. 

9. Include metadata labels when building your image. This action will help in image management: application version, link to website, how to contact the maintainer.

10. Use linting to detect bad practices in the Dockerfile. The most popular linter is [hadolint](https://github.com/hadolint/hadolint).

11. Scan the images to detect potential problems and security issues. It is recommended to scan images every week. 

    There are a lot of popular tools for scanning images: [snyk](http://snyk.io), [trivy](https://github.com/aquasecurity/trivy), [grype](https://github.com/anchore/grype) and etc.


## References:
- https://sysdig.com/blog/dockerfile-best-practices/
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
