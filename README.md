
# Spotify End-to-End Data Engineering Project on Microsoft Azure

## 1. Project Overview

This project implements an end-to-end cloud data engineering solution using Microsoft Azure services to ingest, store, transform, and organize Spotify-related data for analytics.

The solution integrates Azure SQL Database, Azure Data Factory (ADF), Azure Data Lake Storage Gen2 (ADLS Gen2), and Azure Databricks to build a scalable data pipeline following the Medallion Architecture.

Azure Data Factory handles source ingestion, Bronze-layer loading, and pipeline orchestration. Azure Databricks processes and transforms data into Silver and Gold layers using PySpark and Delta Lake. Git integration in both Azure Data Factory and Databricks supports source control and version management.

## 2. Business Use Case

### Business Problem

Music streaming platforms generate data related to users, tracks, artists, albums, and other music catalog entities. This data must be ingested, stored, cleaned, and organized before it can be used effectively for analytics and reporting.

Manual data movement and inconsistent transformation processes can make data maintenance difficult and limit scalability.

### Proposed Solution

Build an automated Azure data pipeline that moves Spotify-related source data from a relational database into a cloud data lake, processes it through multiple data layers, and prepares curated datasets for downstream analytics.

The pipeline separates ingestion from transformation and provides a structured approach to data quality, incremental processing, storage, and deployment management.

### Business Objectives

- Centralize Spotify-related source data in Azure Data Lake Storage Gen2.
- Automate data ingestion and pipeline execution using Azure Data Factory.
- Separate raw, cleansed, and analytics-ready data using the Medallion Architecture.
- Use distributed processing with Azure Databricks and PySpark.
- Improve data consistency and maintainability.
- Maintain pipeline and transformation code using Git integration.
- Establish a foundation for business intelligence and music analytics.

## 3. Architecture

```text
                SOURCE SYSTEM
             Azure SQL Server
             Azure SQL Database
                     |
                     v
            Azure Data Factory
          Ingestion and Orchestration
                     |
                     v
       Azure Data Lake Storage Gen2
                     |
                     v
              BRONZE LAYER
           Raw/Ingested Source Data
                     |
                     v
             Azure Databricks
          PySpark and Delta Lake
                     |
                     v
               SILVER LAYER
        Cleansed and Transformed Data
                     |
                     v
             Azure Databricks
          Business Transformations
                     |
                     v
                GOLD LAYER
          Curated Analytics Datasets
                     |
                     v
         Reporting / Analytics Consumers
```

### Development and Version Control

```text
Azure Data Factory  <---->  Git Repository
Azure Databricks    <---->  Git Repository
```

Git integration allows development changes to be tracked and managed in source control. The exact branch and deployment workflow depends on the configured Git provider and project setup.

## 4. Azure Services and Technologies

| Service / Technology | Role in the Project |
|---|---|
| Azure SQL Server | Hosts the SQL database server |
| Azure SQL Database | Stores the source Spotify-related data |
| Azure Data Factory | Ingests source data, loads the Bronze layer, and orchestrates pipeline execution |
| Azure Data Lake Storage Gen2 | Provides cloud storage for the Bronze, Silver, and Gold layers |
| Azure Databricks | Performs data transformation and processing |
| Apache Spark / PySpark | Supports distributed data processing |
| Delta Lake | Supports reliable storage of processed datasets |
| Unity Catalog | Organizes and governs access to supported data assets |
| Git integration | Tracks and manages ADF and Databricks project changes |
| GitHub | Hosts version-controlled project code and documentation |

## 5. Data Pipeline Implementation

### Step 1: Source Database Setup

Created an Azure SQL Server and an Azure SQL Database to store the source data used by the Spotify data engineering pipeline.

The database serves as the source system from which data is extracted for further processing.

### Step 2: Azure Data Lake Storage Gen2 Setup

Created an Azure Storage account with hierarchical namespace enabled to use Azure Data Lake Storage Gen2.

Organized storage into separate containers or directories for the Medallion layers:

- **Bronze:** Raw ingested data.
- **Silver:** Cleansed and transformed data.
- **Gold:** Curated, analytics-ready data.

### Step 3: Azure Data Factory Pipeline Development

Configured Azure Data Factory to connect to the Azure SQL Database and copy source data into Azure Data Lake Storage Gen2.

ADF is responsible for source ingestion and Bronze-layer loading. It also provides the orchestration framework for coordinating pipeline activities.

### Step 4: Bronze Layer Ingestion

Loaded source data from Azure SQL Database into the Bronze layer of ADLS Gen2 using Azure Data Factory.

The Bronze layer preserves the ingested source data as the starting point for downstream transformations.

### Step 5: Azure Databricks Configuration

Configured the Azure Databricks workspace to access the data lake and process data using Apache Spark and PySpark.

Configured the relevant storage access and Unity Catalog components needed for governed access to the lake.

### Step 6: Silver Layer Transformations

Developed PySpark processing logic in Azure Databricks to transform Bronze data into the Silver layer.

Transformation activities can include:

- Data cleansing and standardization.
- Removing unnecessary columns.
- Deduplicating records using business keys.
- Handling schema changes where configured.
- Writing processed data into Delta tables.
- Managing streaming checkpoints and schema tracking where Auto Loader is used.

### Step 7: Gold Layer Processing

Used Azure Databricks to develop the Gold layer from Silver data.

The Gold layer is intended to contain curated datasets structured for analytical consumption, such as music catalog analysis and other business reporting use cases.

The specific Gold transformations depend on the implemented notebooks and business rules.

### Step 8: Git Integration for Azure Data Factory

Configured Git integration in Azure Data Factory to manage pipeline development through source control.

This supports tracking changes to pipeline definitions and managing collaboration and deployment workflows.

### Step 9: Git Integration for Azure Databricks

Connected Azure Databricks to GitHub and created a Git folder for the project.

This supports version control of notebooks, Python source files, and project configuration files, allowing changes to be committed, pushed, and reviewed.

## 6. Medallion Architecture

| Layer | Technology | Responsibility |
|---|---|---|
| Bronze | Azure Data Factory + ADLS Gen2 | Ingest and retain source data |
| Silver | Azure Databricks + PySpark + Delta Lake | Clean, standardize, deduplicate, and transform data |
| Gold | Azure Databricks + Delta Lake | Prepare curated datasets for analytics |

## 7. Version Control and Development Workflow

The project uses Git integration for both Azure Data Factory and Azure Databricks.

**Azure Data Factory**
- Manage pipeline definitions through the configured Git repository.
- Track pipeline changes.
- Support controlled development and deployment workflows.

**Azure Databricks**
- Maintain notebooks and source code in a Git-connected folder.
- Commit and push code changes.
- Preserve project history and support collaboration.

Git integration provides source control; it does not automatically synchronize all cloud data, workspace permissions, secrets, or service configurations.

## 8. Validation and Testing

The following checks help validate the pipeline:

- Verify connectivity to Azure SQL Database.
- Confirm ADF copy activities load data into the Bronze layer.
- Validate file paths and storage permissions in ADLS Gen2.
- Check source and target schemas and record counts.
- Validate Silver transformations and duplicate handling.
- Confirm Delta tables are created or updated correctly.
- Test Auto Loader behavior and checkpoint management where streaming ingestion is used.
- Verify Gold datasets against the implemented transformation rules.
- Confirm ADF and Databricks changes are committed to their respective Git repositories.

## 9. Business Benefits

- **Centralized storage:** Source and processed data are organized in a common data lake.
- **Automated ingestion:** ADF reduces the need for manual data movement.
- **Scalable processing:** Spark supports distributed data transformations.
- **Improved data quality:** Layered processing supports cleansing and standardization.
- **Reusable architecture:** The pipeline can be extended to additional datasets.
- **Maintainable development:** Git integration provides source history and change tracking.
- **Analytics readiness:** The Gold layer establishes a foundation for downstream BI and reporting.

## 10. Future Enhancements

Potential improvements include:

- Scheduling and monitoring end-to-end pipeline execution.
- Adding automated data quality checks and reconciliation.
- Implementing incremental extraction or change data capture where appropriate.
- Adding CI/CD deployment workflows for ADF and Databricks.
- Connecting Gold datasets to Power BI.
- Adding pipeline logging, alerting, and operational dashboards.
- Implementing more advanced historical tracking and dimensional modeling.

These are proposed enhancements unless they are already implemented in the project.

## 11. Skills Demonstrated

- Microsoft Azure Data Engineering
- Azure SQL Database
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- Apache Spark and PySpark
- Delta Lake
- Medallion Architecture
- Data ingestion and orchestration
- Data cleansing and deduplication
- Incremental and streaming data processing, where configured
- Unity Catalog and cloud storage access
- Git integration and GitHub version control

## 12. Conclusion

This project demonstrates an end-to-end Azure data engineering workflow that connects a relational source database to a cloud data lake and processes data through Bronze, Silver, and Gold layers.

By combining Azure Data Factory, ADLS Gen2, Azure Databricks, PySpark, Delta Lake, and Git integration, the solution establishes a structured and maintainable foundation for data processing and analytics.

**Project category:** End-to-End Data Engineering

**Cloud platform:** Microsoft Azure

**Architecture:** Medallion Architecture

**Source control:** Git integration for Azure Data Factory and Azure Databricks
<img width="1899" height="839" alt="image" src="https://github.com/user-attachments/assets/ad32afaa-6185-4849-ba1d-90d010657ea0" />
<img width="1890" height="776" alt="image" src="https://github.com/user-attachments/assets/6014728a-14a8-4838-8232-88e469961bad" />
<img width="1913" height="766" alt="image" src="https://github.com/user-attachments/assets/b752797b-aabc-47c3-af67-4ed80700a06e" />
<img width="1919" height="919" alt="image" src="https://github.com/user-attachments/assets/7e6a1571-efea-46ae-8812-1c10c1bfadcf" />
<img width="1919" height="898" alt="image" src="https://github.com/user-attachments/assets/2b1c5543-c719-46e7-9314-eb782fbc6523" />

<img width="1898" height="840" alt="image" src="https://github.com/user-attachments/assets/eba751a7-216b-4d1d-982d-c3b69abd5492" />
<img width="1916" height="876" alt="image" src="https://github.com/user-attachments/assets/b270ea43-9be2-4b5a-bdd7-feaa5a201429" />





